from django.urls import path
from . import views

app_name = 'downloads'

urlpatterns = [
    path('request/<int:book_id>/', views.request_download, name='request_download'),
    path('my-requests/', views.my_download_requests, name='my_download_requests'),
    path('approve/<int:request_id>/', views.approve_download_request, name='approve_download_request'),
    path('get/<int:book_id>/', views.download_book, name='download_book'),

]
