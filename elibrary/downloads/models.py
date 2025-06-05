from django.db import models
from django.conf import settings
from books.models import Book  # Assuming you want to track book downloads

class DownloadRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Could be auto-approved or admin-approved

    def __str__(self):
        return f"{self.user.email} requested {self.book.title}"

from django.conf import settings

class Download(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} downloaded {self.book.title} at {self.downloaded_at}"

