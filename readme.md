# BookHive

BookHive is a Django-based web application that provides basic functionality for user and admin login, along with viewing book-related information.

---

## Features (Current)

- User Login page
- User Registration page
- Admin Login page
- Forgot Password page
- Book Detail page
- Admin panel customization

---

## Project Structure
```
BookHive/
│
├── BookhiveProject/
│   ├── settings.py
│   ├── urls.py
│
├── myapp/
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── UserLogin.html
│       ├── UserRegistrations.html
│       ├── UserHome.html
│       ├── AdminLogin.html
│       ├── ForgotPassword.html
│       ├── book_detail.html
│       ├── base.html
│       ├── admin/
│           ├── base_site.html
│
└── manage.py
```
---

## Updated Files in This Version

- myapp/urls.py
- myapp/views.py
- myapp/templates/UserLogin.html
- myapp/templates/ForgotPassword.html
- myapp/templates/AdminLogin.html
- myapp/templates/book_detail.html
- myapp/templates/admin/base_site.html
- myapp/admin.py
- BookhiveProject/settings.py

---

## How to Run

1. Open terminal and go to project folder

2. Create virtual environment:
   python -m venv venv

3. Activate it:
   Mac/Linux: source venv/bin/activate  
   Windows: venv\Scripts\activate

4. Install Django:
   pip install django

5. Apply migrations:
   python manage.py migrate

6. Run server:
   python manage.py runserver

7. Open in browser:
   http://127.0.0.1:8000/

---

## Notes

- Make sure all migrations are applied before running
- File names are case-sensitive (e.g., ForgotPassword.html)
- Admin access requires creating a superuser

To create superuser:
python manage.py createsuperuser

---

## Team

**Team Name:** BookHive Team

- Hemanth Borra  
- Savikhya Kadiyala  
- Harsha Reddy Erragunta  
- Hemesh Phani Sai Bavirisetti  

---
