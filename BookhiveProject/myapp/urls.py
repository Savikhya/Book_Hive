from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegister, name='UserRegister'),
    path('userlogin/', views.UserLogin, name='UserLogin'),
    path('adminlogin/', views.AdminLogin, name='AdminLogin'),
    path('home/', views.UserHome, name='UserHome'),
    path('search/', views.search_books, name='search_books'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('logout/', views.Logout, name='Logout'),
    path('forgotpassword/', views.ForgotPassword, name='ForgotPassword'),
]