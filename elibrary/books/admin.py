# books/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'category', 'is_downloadable', 'upload_date')
    list_filter = ('category', 'is_downloadable', 'upload_date')
    search_fields = ('title', 'author', 'publisher')
