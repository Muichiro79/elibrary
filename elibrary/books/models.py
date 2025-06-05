from django.db import models
from categories.models import Category  # Linking categories

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    description = models.TextField(blank=True)
    is_downloadable = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='books/', blank=True, null=True)  # for the actual book file

    def __str__(self):
        return self.title


