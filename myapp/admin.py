from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created_at']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'published_date']
    list_filter = ['genre', 'author']
    search_fields = ['title', 'isbn']