# BookHive – Digital Library Management System

BookHive is a Django-based digital library web application that allows users to register, log in, search books, view book details, download books, and receive AI-powered book suggestions. The system also includes an admin dashboard where administrators can add, edit, and manage books, genres, PDFs, and cover images.

---

## Project Overview

BookHive is designed to make online book access simple and organized. Users can browse books, search by title, filter by genre, view book details, and download available book files. Admin users can manage the complete book collection through a customized Django admin panel.

The project also integrates a GenAI-powered chatbot using the OpenAI API to help users find books based on their reading interests.

---

## Main Features

### User Features
- User registration
- User login and logout
- Forgot password functionality
- Browse all available books
- Search books by title
- Filter books by genre
- Sort books by title, author, or latest added
- View book details
- View book file
- Download book file
- AI-powered book suggestion chatbot

### Admin Features
- Admin login
- Add new books
- Edit existing books
- Delete books
- Upload book PDFs
- Upload book cover images
- Add and manage genres
- Assign multiple genres to one book
- Customized Django admin interface

### GenAI Chatbot Features
- Suggests books based on user interests
- Uses OpenAI API for intelligent responses
- Matches user input with book title, author, genre, and description
- Can answer questions like:
  - “What genres do you have?”
  - “What books are available?”
  - “Suggest history books”
- Can open books using commands like:
  - `open 1`
  - `open Dracula`
  - `show Hamlet`
- Includes minimize and close options in the chatbot UI

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| Python | Backend programming language |
| Django | Web framework |
| SQLite | Database |
| HTML | Web page structure |
| CSS | Styling and layout |
| JavaScript | Chatbot UI interaction |
| OpenAI API | GenAI chatbot responses |
| Docker | Containerization |
| DockerHub | Image hosting |
| GitHub Actions | CI/CD workflow |
| Git & GitHub | Version control and collaboration |

---

## System Architecture

```text
User / Admin
     ↓
Frontend Templates (HTML + CSS + JavaScript)
     ↓
Django Views (Backend Logic)
     ↓
Models + SQLite Database
     ↓
OpenAI API (GenAI Chatbot)
```

---

## Project Structure

```text
BookHive/
│
├── BookhiveProject/
│   ├── BookhiveProject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── myapp/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── admin/
│   │   │   │   └── base_site.html
│   │   │   ├── AdminLogin.html
│   │   │   ├── UserLogin.html
│   │   │   ├── UserHome.html
│   │   │   ├── UserRegistrations.html
│   │   │   ├── forgotpassword.html
│   │   │   ├── book_detail.html
│   │   │   └── base.html
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── media/
│   │   ├── book_covers/
│   │   └── book_pdfs/
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── README.md
```

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Savikhya/Book_Hive.git
cd Book_Hive/BookhiveProject
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Create `.env` File

Create a `.env` file in the same folder as `manage.py`.

```text
OPENAI_API_KEY=your_api_key_here
```

### Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create Superuser

```bash
python3 manage.py createsuperuser
```

### Run Server

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## GenAI API Integration

BookHive uses the OpenAI API to provide intelligent book recommendations through the chatbot.

```text
User Input → Django Backend → OpenAI API → Response → Chatbot UI
```

The API helps the system understand user interests in natural language and provide more useful book suggestions.

---

## Docker Setup

Build the Docker image:

```bash
docker build -t bookhive-app .
```

Run the container:

```bash
docker run -p 8000:8000 bookhive-app
```

DockerHub Repository:

```text
https://hub.docker.com/r/hemanthborra2212/bookhive-app
```

Pull and run from DockerHub:

```bash
docker pull hemanthborra2212/bookhive-app
docker run -p 8000:8000 hemanthborra2212/bookhive-app
```

---

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD.

The pipeline:
- Installs dependencies
- Runs Django tests
- Verifies that the project works after every push

---

## Team Contributions

### Hemanth
- Project setup and integration
- URL routing
- Docker setup and DockerHub deployment
- Chatbot UI integration

### Savikhya
- Database models
- Book and genre management
- Admin panel customization

### Harsha
- Backend logic
- Search, filter, sort, and pagination
- GenAI chatbot backend functionality

### Hemesh
- UI design
- Login pages
- Book detail page
- View Book and Download Book interface

---

## Conclusion

BookHive is a full-stack digital library management system with user features, admin features, GenAI chatbot integration, Docker deployment, and CI/CD automation.