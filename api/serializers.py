from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """

    class Meta:
        model = Book  # Specifies the model to serialize.
        fields = (
            "__all__"  # Includes all fields of the Book model in the serialization.
        )
