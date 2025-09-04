from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class CustomBookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

       
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Smith", publication_year=2023)

    def test_list_books(self):
        url = reverse("custom-book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("custom-book-detail", kwargs={"pk": self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Basics")

    def test_create_book_authenticated(self):
        url = reverse("custom-book-create")
        data = {"title": "New Book", "author": "Alice", "publication_year": 2024}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse("custom-book-create")
        data = {"title": "Unauthorized", "author": "Bob", "publication_year": 2022}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        url = reverse("custom-book-update", kwargs={"pk": self.book1.pk})
        data = {"title": "Updated Title", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        url = reverse("custom-book-delete", kwargs={"pk": self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        url = reverse("custom-book-list") + "?author=Jane Smith"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Jane Smith")

    def test_search_books(self):
        url = reverse("custom-book-list") + "?search=Advanced"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Advanced Django" in book["title"] for book in response.data))

    def test_order_books(self):
        url = reverse("custom-book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2023)
