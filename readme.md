# BookHive Project

## Overview
BookHive is a web-based application built using Django. The goal of this project is to provide a platform where users can explore, manage, and interact with book-related information.

This project was developed as part of a Scrum-based team assignment, focusing on collaboration, version control using Git, and task management using JIRA.

---

## Features
•⁠  ⁠User Registration and Login
•⁠  ⁠Book browsing interface
•⁠  ⁠Forgot password functionality
•⁠  ⁠Admin login support
•⁠  ⁠Structured Django project setup
•⁠  ⁠Responsive UI using HTML templates

---

## Tech Stack
•⁠  ⁠Backend: Django (Python)
•⁠  ⁠Frontend: HTML, CSS
•⁠  ⁠Database: SQLite
•⁠  ⁠Version Control: Git & GitHub
•⁠  ⁠Project Management: JIRA

---

## Project Structure
Bookhive/
│
├── BookhiveProject/
|
│   ├── BookhiveProject/
|   |
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── myapp/
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── UserRegistrations.html
│   │   │   ├── UserLogin.html
│   │   │   ├── UserHome.html
│   │   │   ├── forgotpassword.html
│   │   │   └── adminlogin.html
│   │   └── migrations/
│   │
│   └── manage.py
│
└── README.md

---

## Setup Instructions

1.⁠ ⁠Clone the repository  
`git clone https://github.com/Savikhya/Book_Hive.git  
cd Book_Hive` 

2.⁠ ⁠Create virtual environment  
`python -m venv venv  
source venv/bin/activate   (Mac/Linux)  
venv\Scripts\activate      (Windows)`  

3.⁠ ⁠Install dependencies  
`pip install django`  

4.⁠ ⁠Run migrations  
`python manage.py migrate`  

5.⁠ ⁠Start server  
`python manage.py runserver`  

6.⁠ ⁠Open in browser  
`http://127.0.0.1:8000/home/`

---

## Team Members & Responsibilities

### Member 1 – Hemanth Borra
•⁠  ⁠manage.py  
•⁠  ⁠settings.py  
•⁠  ⁠urls.py  
•⁠  ⁠asgi.py  
•⁠  ⁠wsgi.py  
•⁠  ⁠apps.py  

---

### Member 2 – Savikhya Kadiyala
•⁠  ⁠models.py  
•⁠  ⁠migrations  
•⁠  ⁠admin.py  
•⁠  ⁠UserRegistrations.html  
•⁠  ⁠Registration logic  

---

### Member 3 – Harsha Reddy Erragunta
•⁠  ⁠UserLogin.html  
•⁠  ⁠UserHome.html  
•⁠  ⁠forgotpassword.html  
•⁠  ⁠Login/Logout logic  
•⁠  ⁠views.py  

---

### Member 4 – Hemesh Phani Sai Bavirisetti
•⁠  ⁠base.html  
•⁠  ⁠adminlogin.html  
•⁠  ⁠tests.py  
•⁠  ⁠README.md  

---

## Git Workflow
•⁠  ⁠Each member worked on separate branches
•⁠  ⁠Member 1 used branch: project_setup
•⁠  ⁠Changes were committed with meaningful messages
•⁠  ⁠Pull requests were created and reviewed before merging
•⁠  ⁠Collaboration was done using GitHub

---

## Important Instructions

The following files and folders should NOT be pushed to the repository:
•⁠  ⁠venv/  
•⁠  ⁠db.sqlite3  

---

## License
This project is for academic purposes only.
