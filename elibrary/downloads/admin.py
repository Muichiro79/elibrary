from django.contrib import admin
from .models import DownloadRequest

@admin.action(description="✅ Approve selected download requests")
def approve_requests(modeladmin, request, queryset):
    updated = queryset.update(approved=True)
    modeladmin.message_user(request, f"{updated} request(s) approved.")

@admin.register(DownloadRequest)
class DownloadRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'approved', 'requested_at')
    list_filter = ('approved', 'requested_at')
    search_fields = ('user__username', 'book__title')
    actions = [approve_requests]
    list_editable = ('approved',)  # Optional: allows quick toggle from the list view
