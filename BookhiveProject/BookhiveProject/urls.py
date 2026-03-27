from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.UserLogin, name='Root'),
    path('admin/', admin.site.urls),
    path('register/', views.UserRegister, name='UserRegister'),
    path('userlogin/', views.UserLogin, name='UserLogin'),
    path('adminlogin/', views.AdminLogin, name='AdminLogin'),
    path('home/', views.UserHome, name='UserHome'),
    path('logout/', views.Logout, name='Logout'),
    path('forgotpassword/', views.ForgotPassword, name='ForgotPassword'),
    path('home/', views.UserHome, name='UserHome'),
    path('search/', views.search_books, name='search_books'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
]