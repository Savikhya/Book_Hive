from django.contrib import admin
from .models import Book, Genre, UserRegistrationModel

admin.site.site_header = 'Bookhive Administration'
admin.site.site_title = 'Bookhive Admin'
admin.site.index_title = 'Bookhive Administration'


@admin.register(UserRegistrationModel)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'loginid', 'email', 'mobile', 'city', 'state')
    search_fields = ('name', 'loginid', 'email', 'mobile')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'book_pdf')
    search_fields = ('title', 'author', 'genre__name')
    list_filter = ('genre',)