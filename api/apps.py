from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Use BigAutoField for auto-generated primary keys
    name = 'api'  # Name of the Django app
