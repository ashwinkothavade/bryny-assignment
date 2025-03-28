from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .models import ServiceRequest, CustomerProfile
from .forms import ServiceRequestForm, CommentForm, CustomerRegistrationForm, CustomerProfileForm

def is_staff_user(user):
    return user.is_staff

def is_customer(user):
    return not user.is_staff

def register_customer(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_staff:
        # Staff view - show all requests with filters
        status_filter = request.GET.get('status', '')
        priority_filter = request.GET.get('priority', '')
        search_query = request.GET.get('search', '')

        requests = ServiceRequest.objects.all()
        
        if status_filter:
            requests = requests.filter(status=status_filter)
        if priority_filter:
            requests = requests.filter(priority=priority_filter)
        if search_query:
            requests = requests.filter(
                Q(customer__username__icontains=search_query) |
                Q(customer__customerprofile__customer_id__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        requests = requests.order_by('-priority', '-created_at')
    else:
        # Customer view - show only their requests
        requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    
    context = {
        'requests': requests,
        'status_choices': ServiceRequest.STATUS_CHOICES,
        'priority_choices': ServiceRequest.PRIORITY_CHOICES,
    }
    return render(request, 'service_requests/dashboard.html', context)

@login_required
@user_passes_test(is_customer)
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            
            # Set priority based on request type
            if service_request.request_type == 'gas_leak' or service_request.request_type == 'emergency':
                service_request.priority = 'urgent'
            
            service_request.save()
            messages.success(request, 'Service request created successfully! Our team will review it shortly.')
            return redirect('request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    # Check if user has permission to view this request
    if not request.user.is_staff and request.user != service_request.customer:
        raise PermissionDenied("You do not have permission to view this request.")
    
    if request.method == 'POST' and not request.user.is_staff:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.service_request = service_request
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('request_detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'service_requests/request_detail.html', {
        'request': service_request,
        'comment_form': comment_form if not request.user.is_staff else None,
    })

@login_required
@user_passes_test(is_staff_user)
def update_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    new_status = request.POST.get('status')
    
    if new_status in dict(ServiceRequest.STATUS_CHOICES):
        old_status = service_request.status
        service_request.status = new_status
        
        if new_status == 'resolved':
            service_request.resolved_at = timezone.now()
        
        # Assign the request to the staff member who updates it
        if old_status == 'pending' and new_status == 'in_progress':
            service_request.assigned_to = request.user
        
        service_request.save()
        messages.success(request, f'Request status updated to {service_request.get_status_display()}')
    return redirect('request_detail', pk=pk)

@login_required
@user_passes_test(is_customer)
def profile(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=request.user.customerprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = CustomerProfileForm(instance=request.user.customerprofile)
    
    context = {
        'form': form,
        'profile': request.user.customerprofile
    }
    return render(request, 'service_requests/profile.html', context)
