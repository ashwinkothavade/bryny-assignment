# Gas Utility Service Request System

A Django-based web application for managing gas utility service requests. This system allows customers to submit and track service requests while providing staff members with tools to manage and respond to these requests effectively.

## Features

### For Customers
- User registration and authentication
- Submit service requests with priority levels
- Track request status
- Add comments to existing requests
- Update profile information
- View request history
- File attachment support for requests

### For Staff (Admin)
- Comprehensive dashboard to view all requests
- Filter and search requests by status, priority, and customer details
- Update request status
- View customer information
- Track communication history
- Automatic priority assignment for emergencies

## Technical Stack

- Python 3.8+
- Django 4.2.12
- Bootstrap 4
- Crispy Forms
- SQLite (default database)

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the application at http://127.0.0.1:8000/
2. Register as a customer at http://127.0.0.1:8000/register/
3. Admin interface available at http://127.0.0.1:8000/admin/

## Codebase Structure

```
bynry_assignment/
│
├── gas_utility/                 # Project configuration directory
│   ├── __init__.py
│   ├── settings.py             # Project settings and configurations
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── service_requests/           # Main application directory
│   ├── migrations/            # Database migrations
│   ├── static/               # Static files
│   │   ├── css/
│   │   │   └── custom.css    # Custom styling
│   │   └── img/
│   │       └── favicon.svg   # Application icon
│   │
│   ├── templates/            # HTML templates
│   │   ├── registration/
│   │   │   ├── login.html    # User login template
│   │   │   └── register.html # User registration template
│   │   │
│   │   └── service_requests/
│   │       ├── base.html     # Base template with common elements
│   │       ├── dashboard.html # Main dashboard view
│   │       ├── create_request.html # Service request form
│   │       ├── request_detail.html # Request details view
│   │       └── profile.html  # User profile page
│   │
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py             # Application configuration
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── urls.py             # Application URL routing
│   └── views.py            # View logic
│
├── media/                   # User-uploaded files
├── staticfiles/            # Collected static files
├── .gitignore             # Git ignore rules
├── manage.py              # Django management script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

### Key Components

1. **Models** (`models.py`):
   - `CustomerProfile`: Extended user profile with customer details
   - `ServiceRequest`: Service request data structure
   - `Comment`: Communication thread for requests

2. **Views** (`views.py`):
   - Customer registration and authentication
   - Dashboard views for staff and customers
   - Service request management
   - Profile management

3. **Forms** (`forms.py`):
   - User registration forms
   - Service request forms
   - Profile update forms
   - Comment forms

4. **Templates**:
   - Responsive Bootstrap-based layouts
   - Role-based UI components
   - Modern design with custom CSS

5. **Static Files**:
   - Custom CSS for enhanced UI
   - SVG favicon and icons
   - Third-party libraries (Bootstrap, Font Awesome)
