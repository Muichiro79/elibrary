from django.urls import path
from . import views



app_name = 'dashboards' 

urlpatterns = [
    # Admin
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/download-requests/', views.admin_download_requests, name='admin_download_requests'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),

    # User
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('user/my-downloads/', views.user_downloads, name='user_downloads'),
    path('user/profile/', views.user_profile, name='user_profile'),
]
