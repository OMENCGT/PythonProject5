from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON_FICTION', 'Non-Fiction'),
        ('SCIENCE', 'Science'),
        ('HISTORY', 'History'),
        ('BIOGRAPHY', 'Biography'),
        ('FANTASY', 'Fantasy'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    page_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
