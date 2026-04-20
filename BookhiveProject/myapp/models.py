from django.db import models


class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    locality = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.loginid


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    book_pdf = models.FileField(upload_to='book_pdfs/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title