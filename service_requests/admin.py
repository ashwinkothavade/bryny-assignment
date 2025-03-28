from django.contrib import admin
from .models import ServiceRequest, Comment

# Register your models here.

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('request_type', 'customer', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type')
    search_fields = ('customer__username', 'customer__email', 'description')
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username', 'service_request__description')
