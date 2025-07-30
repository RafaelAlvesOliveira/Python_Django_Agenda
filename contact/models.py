from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name: models.CharField = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name: models.CharField = models.CharField(max_length=50)
    last_name: models.CharField = models.CharField(max_length=50, blank=True)
    phone: models.CharField = models.CharField(max_length=50)
    email: models.EmailField = models.EmailField(max_length=254, blank=True)
    created_date: models.DateTimeField = models.DateTimeField(
        default=timezone.now)
    description: models.TextField = models.TextField(blank=True)
    show: models.BooleanField = models.BooleanField(default=True)
    picture: models.ImageField = models.ImageField(
        blank=True, upload_to='pictures/%Y/%m/')
    category: models.ForeignKey = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
