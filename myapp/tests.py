import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book

class AuthorTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author_data = {
            'name': 'Test Author',
            'birth_date': '1980-01-01',
            'bio': 'Test biography'
        }
        self.author = Author.objects.create(**self.author_data)
        self.url = '/api/author'

    def test_create_author(self):
        response = self.client.post(self.url, self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.assertEqual(Author.objects.count(), 2)

    def test_get_author(self):
        url = '/api/author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json.loads(response.content)), type(list()))

    def test_update_author(self):
        url = '/api/author'
        response = self.client.get(url)
        data = json.loads(response.content)
        pk = data[0]['id']
        url = '/api/author/' + str(pk)
        updated_data = {'name': 'Updated Author'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author')

    def test_delete_author(self):
        url = '/api/author'
        response = self.client.get(url)
        data = json.loads(response.content)
        pk = data[0]['id']

        url = '/api/author/' + str(pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Author.objects.count(), 0)

class BookTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Test Author')
        self.book_data = {
            'title': 'Test Book',
            'author': self.author.id,
            'isbn': '1234567890123',
            'published_date': '2023-01-01',
            'genre': 'FICTION',
            'description': 'Test description',
            'page_count': 100
        }
        self.book = Book.objects.create(
            title='Existing Book',
            author=self.author,
            isbn='9876543210987',
            published_date='2023-01-01',
            genre='FICTION',
            page_count=200
        )
        self.url = '/api/book'

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book(self):
        url = '/api/book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json.loads(response.content)), type(list()))

    def test_update_book(self):
        url = '/api/book'
        response = self.client.get(url)
        data = json.loads(response.content)
        pk = data[0]['id']

        url = '/api/book/' + str(pk)
        updated_data = {'title': 'Updated book'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated book')

    def test_delete_book(self):
        url = '/api/book'
        response = self.client.get(url)
        data = json.loads(response.content)
        pk = data[0]['id']

        url = '/api/book/' + str(pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Book.objects.count(), 0)
