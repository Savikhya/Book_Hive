from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, UserRegistrationModel


# ---------------- REGISTER ----------------
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


# ---------------- LOGIN ----------------
def UserLogin(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        password = request.POST.get('pswd')

        user = UserRegistrationModel.objects.filter(
            loginid=loginid,
            password=password,
        ).first()

        if user:
            request.session['user_loginid'] = user.loginid
            return redirect('UserHome')

        messages.error(request, 'Invalid Login ID or Password')

    return render(request, 'UserLogin.html')


# ---------------- USER HOME + SEARCH ----------------
def UserHome(request):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    query = request.GET.get('q', '').strip()
    books = Book.objects.select_related('genre').all()

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(genre__name__icontains=query)
            | Q(description__icontains=query)
        )

    context = {
        'books': books,
        'query': query,
    }
    return render(request, 'UserHome.html', context)


# Separate search URL that reuses the same page
def search_books(request):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    return UserHome(request)


# ---------------- BOOK DETAIL PAGE ----------------
def book_detail(request, id):
    if 'user_loginid' not in request.session:
        return redirect('UserLogin')

    book = get_object_or_404(Book.objects.select_related('genre'), id=id)
    return render(request, 'book_detail.html', {'book': book})


# ---------------- LOGOUT ----------------
def Logout(request):
    request.session.flush()
    return redirect('UserLogin')


# ---------------- ADMIN LOGIN ----------------
def AdminLogin(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        password = request.POST.get('pswd')

        if loginid == 'admin' and password == 'admin':
            messages.success(request, 'Admin login successful')
            return render(request, 'AdminLogin.html')

        messages.error(request, 'Invalid admin credentials')

    return render(request, 'AdminLogin.html')


# ---------------- FORGOT PASSWORD ----------------
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