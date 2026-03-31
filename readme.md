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
```
Bookhive/
│
├── BookhiveProject/
│   ├── BookhiveProject/
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
```
---

## Setup Instructions

1.⁠ ⁠Clone the repository  

`git clone https://github.com/Savikhya/Book_Hive.git` 

`cd Book_Hive` 

2.⁠ ⁠Create virtual environment 

`python -m venv venv`  

`source venv/bin/activate`   #(Mac/Linux)

`venv\Scripts\activate`      #(Windows)  

3.⁠ ⁠Install dependencies  
`pip install django`  

4.⁠ ⁠Run migrations  
`python manage.py migrate`  

5.⁠ ⁠Start server  
`python manage.py runserver`  

6.⁠ ⁠Open in browser  
`http://127.0.0.1:8000/home/`

---

## Important Instructions

The following files and folders should NOT be pushed to the repository:

•⁠  ⁠venv/  
•⁠  ⁠db.sqlite3  

---
## Notes

This README covers Sprint 1 only. It will be updated at each new sprint to reflect newly added features, any changes to setup, and updated project structure.

-------

## License
This project is for academic purposes only.
