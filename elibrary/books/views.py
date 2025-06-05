from django.shortcuts import render, get_object_or_404
from .models import Book
from categories.models import Category
from django.db.models import Q

def book_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')
    
    books = Book.objects.all()
    
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query)
        )
    
    if category_id:
        books = books.filter(category_id=category_id)
    
    categories = Category.objects.all()
    
    context = {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
