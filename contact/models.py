from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Contact(models.Model):
    first_name: models.CharField = models.CharField(max_length=50)
    last_name: models.CharField = models.CharField(max_length=50, blank=True)
    phone: models.CharField = models.CharField(max_length=50)
    email: models.EmailField = models.EmailField(max_length=254, blank=True)
    created_date: models.DateTimeField = models.DateTimeField(
        default=timezone.now)
    description: models.TextField = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
