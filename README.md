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

## Project Structure

- `service_requests/` - Main application directory
  - `models.py` - Database models for requests and profiles
  - `views.py` - View logic and request handling
  - `forms.py` - Form definitions
  - `urls.py` - URL routing
  - `templates/` - HTML templates
  - `admin.py` - Admin interface configuration

## Security Features

- Role-based access control
- CSRF protection
- Password validation
- Secure file uploads
- Request validation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
