from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.

    Provides functionalities to list, create, retrieve, update, and delete books.
    Inherits from viewsets.ModelViewSet to handle standard CRUD operations.

    Attributes:
        queryset (QuerySet): QuerySet of all Book objects.
        serializer_class (class): Serializer class to convert Book instances to JSON.
    """

    queryset = Book.objects.all()  # Retrieves all Book objects from the database.
    serializer_class = (
        BookSerializer  # Specifies the serializer class for Book instances.
    )
