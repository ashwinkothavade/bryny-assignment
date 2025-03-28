from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    customer_id = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        CustomerProfile.objects.create(user=instance)
        # Generate a customer ID (e.g., CUST001)
        last_profile = CustomerProfile.objects.exclude(customer_id=None).order_by('-customer_id').first()
        if last_profile:
            last_id = int(last_profile.customer_id[4:])
            new_id = f"CUST{str(last_id + 1).zfill(3)}"
        else:
            new_id = "CUST001"
        instance.customerprofile.customer_id = new_id
        instance.customerprofile.save()

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('connection', 'New Connection'),
        ('billing', 'Billing Issue'),
        ('maintenance', 'Maintenance'),
        ('meter_reading', 'Meter Reading'),
        ('emergency', 'Emergency Service'),
        ('other', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username} - {self.status}"

class Comment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.service_request}"
