from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import DownloadRequest
from downloads.models import Download

from django.contrib import messages

@login_required
def request_download(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if user already requested
    if DownloadRequest.objects.filter(user=request.user, book=book).exists():
        messages.info(request, "You already requested this download.")
        return redirect('books:book_detail', pk=book.pk)  # Or wherever your book detail page is

    # Create download request
    DownloadRequest.objects.create(user=request.user, book=book, approved=False)
    messages.success(request, "Download request sent. Wait for approval.")
    return redirect('books:book_detail', pk=book.pk)


@login_required
def my_download_requests(request):
    requests = DownloadRequest.objects.filter(user=request.user)
    return render(request, 'downloads/my_requests.html', {'requests': requests})

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from .models import DownloadRequest
from django.contrib import messages

@staff_member_required
def approve_download_request(request, request_id):
    download_request = get_object_or_404(DownloadRequest, id=request_id)
    download_request.approved = True
    download_request.save()
    messages.success(request, f"Download request #{request_id} approved.")
    return redirect('admin:downloads_downloadrequest_changelist')  # Redirect to admin list page


from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import DownloadRequest
from books.models import Book

@login_required
def download_book(request, book_id):
    try:
        req = DownloadRequest.objects.get(user=request.user, book_id=book_id, approved=True)
        book = req.book
        if not book.file:
            raise Http404("No file attached to this book.")
        return FileResponse(book.file.open('rb'), as_attachment=True, filename=book.file.name)
    except DownloadRequest.DoesNotExist:
        raise Http404("Download not approved.")

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from books.models import Book
from downloads.models import DownloadRequest

@login_required
def download_book_text(request, book_id):
    # Check approval
    try:
        DownloadRequest.objects.get(user=request.user, book_id=book_id, approved=True)
    except DownloadRequest.DoesNotExist:
        raise Http404("Download not approved.")

    book = Book.objects.get(id=book_id)
    
    if not book.content:  # assuming 'content' is your text field
        raise Http404("No content available to download.")

    response = HttpResponse(book.content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{book.title}.txt"'
    return response


@login_required
def user_downloads(request):
    downloads = Download.objects.filter(user=request.user).order_by('-downloaded_at')
    return render(request, 'dashboards/user_downloads.html', {'downloads': downloads})
