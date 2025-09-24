from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')