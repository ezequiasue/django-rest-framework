from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTestCase(TestCase):

    def setUp(self):
        Book.objects.create(
            title="Sample Book",
            author="John Doe",
            published_date="2023-01-01",
            isbn="9780123456789",
        )

    def test_book_model(self):
        book = Book.objects.get(title="Sample Book")
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.published_date.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(book.isbn, "9780123456789")

    def test_books_list_view(self):
        response = self.client.get(reverse("books-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")
        self.assertTemplateUsed(response, "books-list")
