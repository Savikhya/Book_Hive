from django.contrib import admin
from django.utils.html import format_html
from .models import Book, Genre, UserRegistrationModel

admin.site.site_header = 'BookHive Administration'
admin.site.site_title = 'BookHive Admin'
admin.site.index_title = 'BookHive Dashboard'


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
    list_display = ('id', 'title', 'author', 'get_genres', 'book_pdf', 'cover_image', 'edit_link')
    search_fields = ('title', 'author', 'genres__name')
    list_filter = ('genres',)
    ordering = ('title',)
    filter_horizontal = ('genres',)

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = 'Genres'

    def edit_link(self, obj):
        return format_html('<a href="/admin/myapp/book/{}/change/">Edit</a>', obj.id)
    edit_link.short_description = 'Edit'