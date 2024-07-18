from django.db import models


class Book(models.Model):
    """
    Model representing a book.
    """

    title = models.CharField(max_length=255)  # Title of the book.
    author = models.CharField(max_length=100)  # Author(s) of the book.
    published_date = models.DateField()  # Date when the book was published.
    isbn = models.CharField(max_length=13)  # ISBN code of the book.

    def __str__(self):
        return self.title
