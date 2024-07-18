# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Supondo que o ViewSet correto seja BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # Registrando o ViewSet para o modelo Book

urlpatterns = [
    path('', include(router.urls)),
]
