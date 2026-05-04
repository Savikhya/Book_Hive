import os
from dotenv import load_dotenv
from openai import OpenAI
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, Genre, UserRegistrationModel


STOPWORDS = {
    'i', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'she', 'they', 'them',
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'so', 'because',
    'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being',
    'want', 'need', 'like', 'love', 'prefer', 'interested', 'interest',
    'book', 'books', 'something', 'about', 'with', 'for', 'on', 'of', 'to',
    'that', 'this', 'these', 'those', 'in', 'at', 'by', 'from', 'as',
    'please', 'can', 'could', 'would', 'should', 'give', 'suggest', 'show',
    'find', 'looking', 'look', 'tell', 'into', 'more', 'some', 'any', 'kind',
    'read', 'reading'
}


def normalize_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_keywords(text):
    cleaned = normalize_text(text)
    words = cleaned.split()
    return [word for word in words if word not in STOPWORDS and len(word) > 2]


def extract_author_hint(text):
    cleaned = normalize_text(text)
    match = re.search(r'\bby\s+([a-z0-9\s]+)', cleaned)
    if match:
        author_hint = match.group(1).strip()
        author_hint = re.sub(r'\b(about|with|that|which|who|where|and|or)\b.*$', '', author_hint).strip()
        return author_hint
    return ""


def score_book_against_interest(book, user_message):
    cleaned_message = normalize_text(user_message)
    keywords = extract_keywords(user_message)
    author_hint = extract_author_hint(user_message)

    title_text = normalize_text(book.title)
    author_text = normalize_text(book.author)
    description_text = normalize_text(book.description)
    genre_text = normalize_text(" ".join([g.name for g in book.genres.all()]))

    score = 0
    reasons = []

    if cleaned_message and len(cleaned_message.split()) >= 2:
        if cleaned_message in description_text:
            score += 15
            reasons.append("description phrase match")
        if cleaned_message in title_text:
            score += 10
            reasons.append("title phrase match")
        if cleaned_message in genre_text:
            score += 8
            reasons.append("genre phrase match")
        if cleaned_message in author_text:
            score += 7
            reasons.append("author phrase match")

    if author_hint and author_hint in author_text:
        score += 14
        reasons.append("author requested")

    for word in keywords:
        if word in description_text:
            score += 6
            if "description keywords" not in reasons:
                reasons.append("description keywords")
        if word in genre_text:
            score += 4
            if "genre match" not in reasons:
                reasons.append("genre match")
        if word in title_text:
            score += 3
            if "title match" not in reasons:
                reasons.append("title match")
        if word in author_text:
            score += 3
            if "author match" not in reasons:
                reasons.append("author match")

    return score, reasons


def UserRegister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        loginid = request.POST.get('loginid')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')

        if UserRegistrationModel.objects.filter(loginid=loginid).exists():
            messages.error(request, 'Login ID already exists')
            return render(request, 'UserRegistrations.html')

        UserRegistrationModel.objects.create(
            name=name,
            loginid=loginid,
            password=password,
            mobile=mobile,
            email=email,
            locality=locality,
            address=address,
            city=city,
            state=state,
        )

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('UserLogin')

    return render(request, 'UserRegistrations.html')


def UserLogin(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        password = request.POST.get('pswd')

        user = UserRegistrationModel.objects.filter(
            loginid=loginid,
            password=password
        ).first()

        if user:
            request.session['user_loginid'] = user.loginid
            return redirect('UserHome')

        messages.error(request, 'Invalid Login ID or Password')

    return render(request, 'UserLogin.html')


def UserHome(request):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    query = request.GET.get('q', '').strip()
    selected_genre = request.GET.get('genre', '').strip()
    sort_by = request.GET.get('sort', '').strip()

    books = Book.objects.prefetch_related('genres').all().distinct()
    genres = Genre.objects.all().order_by('name')

    if query:
        books = books.filter(title__icontains=query).distinct()

    if selected_genre:
        books = books.filter(genres__id=selected_genre).distinct()

    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    elif sort_by == 'latest':
        books = books.order_by('-id')
    else:
        books = books.order_by('title')

    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    suggestions = []
    if (query or selected_genre) and not page_obj.object_list:
        suggestions = [
            'Check the spelling of the book title.',
            'Try a shorter keyword.',
            'Use the Clear button to see all books again.'
        ]

    context = {
        'books': page_obj,
        'page_obj': page_obj,
        'query': query,
        'genres': genres,
        'selected_genre': selected_genre,
        'sort_by': sort_by,
        'suggestions': suggestions,
    }
    return render(request, 'UserHome.html', context)


def search_books(request):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')
    return UserHome(request)


def book_detail(request, id):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    book = get_object_or_404(Book.objects.prefetch_related('genres'), id=id)

    same_author_books = Book.objects.filter(
        author__iexact=book.author
    ).exclude(id=book.id).prefetch_related('genres').distinct()[:4]

    same_author_ids = [b.id for b in same_author_books]
    current_genre_ids = book.genres.values_list('id', flat=True)
    remaining_slots = 4 - len(same_author_ids)

    same_genre_books = Book.objects.none()
    if remaining_slots > 0:
        same_genre_books = Book.objects.filter(
            genres__in=current_genre_ids
        ).exclude(
            id=book.id
        ).exclude(
            id__in=same_author_ids
        ).prefetch_related('genres').distinct()[:remaining_slots]

    recommended_books = list(same_author_books) + list(same_genre_books)

    return render(request, 'book_detail.html', {
        'book': book,
        'recommended_books': recommended_books,
    })


from django.http import JsonResponse

from django.http import JsonResponse
from .models import Book

def chatbot_suggestions(request):
    if 'user_loginid' not in request.session:
        return JsonResponse({
            "reply": "Please login first.",
            "books": [],
            "redirect_url": ""
        })

    user_message = request.GET.get("message", "").strip()

    if not user_message:
        return JsonResponse({
            "reply": "What are you interested in reading?",
            "books": [],
            "redirect_url": ""
        })

    # Open book command
    message_lower = user_message.lower()
    if "open" in message_lower or "show" in message_lower or "go to" in message_lower:
        number_match = re.search(r'\b(\d+)(st|nd|rd|th)?\b', message_lower)

        if number_match:
            number = int(number_match.group(1))
            last_book_ids = request.session.get("last_chatbot_book_ids", [])

            if 1 <= number <= len(last_book_ids):
                book = Book.objects.filter(id=last_book_ids[number - 1]).first()
                if book:
                    return JsonResponse({
                        "reply": f"Opening {book.title}.",
                        "books": [],
                        "redirect_url": f"/book/{book.id}/"
                    })

        cleaned_title = message_lower
        for word in ["open", "show", "go to", "take me to"]:
            cleaned_title = cleaned_title.replace(word, "")
        cleaned_title = cleaned_title.strip()

        matched_book = Book.objects.filter(title__icontains=cleaned_title).first()

        if matched_book:
            return JsonResponse({
                "reply": f"Opening {matched_book.title}.",
                "books": [],
                "redirect_url": f"/book/{matched_book.id}/"
            })

    # Get available books from database
    all_books = Book.objects.prefetch_related("genres").all()

    book_context = ""
    for book in all_books:
        genres = ", ".join([g.name for g in book.genres.all()])
        book_context += (
            f"Title: {book.title}\n"
            f"Author: {book.author}\n"
            f"Genres: {genres}\n"
            f"Description: {book.description}\n\n"
        )

    # Save conversation history
    chat_history = request.session.get("chat_history", [])

    chat_history.append({
        "role": "user",
        "content": user_message
    })

    # Keep only last 6 messages so it does not become too long
    chat_history = chat_history[-6:]

    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are BookHive's friendly book recommendation chatbot. "
                    "Answer like a real chatbot. Be conversational, helpful, and short. "
                    "Use ONLY the books from the BookHive library listed below. "
                    "Do not invent books outside this list. "
                    "If the user asks what books or genres are available, answer from the list. "
                    "If recommending books, mention book titles clearly and briefly explain why they match.\n\n"
                    f"BookHive Library:\n{book_context}"
                )
            }
        ] + chat_history

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=220
        )

        reply = response.choices[0].message.content

        # ✅ Clean formatting
        reply = reply.replace("**", "")

        import re
        reply = re.sub(r'(\d+\.)', r'\n\1', reply)

        reply = reply.strip()

        chat_history.append({
            "role": "assistant",
            "content": reply
        })

        request.session["chat_history"] = chat_history
        request.session.modified = True

    except Exception as e:
        reply = "Sorry, I could not connect to the AI service right now. Please try again."

    # Find matching books from database to display as clickable links
    keywords = extract_keywords(user_message)
    matched_books = []

    for book in all_books:
        score = 0
        title = normalize_text(book.title)
        author = normalize_text(book.author)
        description = normalize_text(book.description)
        genres = normalize_text(" ".join([g.name for g in book.genres.all()]))

        for word in keywords:
            if word in genres:
                score += 10
            if word in description:
                score += 6
            if word in title:
                score += 4
            if word in author:
                score += 2

        if score > 0:
            matched_books.append((score, book))

    matched_books.sort(key=lambda x: (-x[0], x[1].title))
    top_books = [book for score, book in matched_books[:5]]

    request.session["last_chatbot_book_ids"] = [book.id for book in top_books]

    books_data = []
    for book in top_books:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genres": ", ".join([g.name for g in book.genres.all()]),
            "description": book.description[:150] + "..." if len(book.description) > 150 else book.description,
            "matched_on": "Matched with your reading interest"
        })

    return JsonResponse({
        "reply": reply,
        "books": books_data,
        "redirect_url": ""
    })


def download_book_pdf(request, id):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    book = get_object_or_404(Book, id=id)

    if not book.book_pdf:
        raise Http404("PDF not found")

    return FileResponse(
        book.book_pdf.open('rb'),
        as_attachment=True,
        filename=book.book_pdf.name.split('/')[-1]
    )


def Logout(request):
    request.session.flush()
    logout(request)
    return redirect('UserLogin')


def AdminLogin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/admin/')

    if request.method == 'POST':
        username = request.POST.get('loginid')
        password = request.POST.get('pswd')

        admin_user = authenticate(request, username=username, password=password)

        if admin_user and admin_user.is_staff:
            login(request, admin_user)
            messages.success(request, 'Admin login successful')
            return redirect('/admin/')

        messages.error(request, 'Invalid admin username or password')

    return render(request, 'AdminLogin.html')


def ForgotPassword(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'ForgotPassword.html')

        user = UserRegistrationModel.objects.filter(
            loginid=loginid,
            email=email,
        ).first()

        if user:
            user.password = new_password
            user.save()
            messages.success(request, 'Password reset successful. Please login.')
            return redirect('UserLogin')

        messages.error(request, 'Invalid Login ID or Email')

    return render(request, 'ForgotPassword.html')