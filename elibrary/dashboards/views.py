from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from downloads.models import DownloadRequest

# Helper to check if user is admin
def is_admin(user):
    return user.is_staff

# --- ADMIN VIEWS ---

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    # You can add more admin stats here
    return render(request, 'dashboards/admin_dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_download_requests(request):
    # List all pending and approved download requests
    requests = DownloadRequest.objects.all().order_by('-requested_at')
    return render(request, 'dashboards/admin_download_requests.html', {'requests': requests})

@login_required
@user_passes_test(is_admin)
def admin_profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Your password has been updated.')
            return redirect('admin_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboards/admin_profile.html', {'form': form})

# --- USER VIEWS ---

@login_required
def user_dashboard(request):
    # Add any user-specific dashboard info here
    return render(request, 'dashboards/user_dashboard.html')

@login_required
def user_downloads(request):
    # Show downloads approved for this user
    downloads = DownloadRequest.objects.filter(user=request.user).order_by('-requested_at')

    return render(request, 'dashboards/user_downloads.html', {'downloads': downloads})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboards/user_profile.html', {'form': form})
