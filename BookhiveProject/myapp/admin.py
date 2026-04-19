from django.contrib import admin
from django.utils.html import format_html
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
    list_display = ('id', 'title', 'author', 'genre', 'book_pdf', 'cover_image', 'edit_link')
    search_fields = ('title', 'author', 'genre__name')
    list_filter = ('genre',)
    ordering = ('title',)

    def edit_link(self, obj):
        return format_html('<a href="/admin/myapp/book/{}/change/">Edit</a>', obj.id)

    edit_link.short_description = 'Edit'