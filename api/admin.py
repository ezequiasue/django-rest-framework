# api/admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)  # Register the Book model with the Django admin
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "published_date",
        "isbn",
    )  # Fields to display in the admin list view

    search_fields = (
        "title",
        "author",
        "isbn",
    )  # Enable search functionality for specified fields

    list_filter = (
        "author",
        "published_date",
    )  # Filters for specified fields in the admin sidebar

    # Additional configurations can be added here as needed
