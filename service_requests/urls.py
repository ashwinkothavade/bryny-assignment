from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_customer, name='register'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create_request, name='create_request'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('request/<int:pk>/update-status/', views.update_request_status, name='update_request_status'),
]
