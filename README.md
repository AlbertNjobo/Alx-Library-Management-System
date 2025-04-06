# Alx Library Management System

## Overview
The Alx Library Management System is a Django-based web application designed to manage library operations, including book borrowing, returning, and user management. It provides features for both regular users and administrators.

## Features
### User Features
- User registration and login.
- View available books.
- Search and filter books by title, author, or availability.
- Borrow books (check-out functionality).
- Return books (return functionality).
- View borrowing history.

### Admin Features
- Admin dashboard with an overview of books, users, and transactions.
- Manage books (add, update, delete).
- View and manage transactions.
- Send email notifications for overdue books.

## Installation
### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- A virtual environment tool (e.g., `venv`)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Alx-Library-Management-System
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## Deployment
### Steps
1. Update `settings.py` for production:
   - Set `DEBUG = False`.
   - Add your domain to `ALLOWED_HOSTS`.

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Use a production server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn library_api.wsgi:application --bind 0.0.0.0:8000
   ```

4. Configure a reverse proxy (e.g., Nginx) to serve the application.

## Testing
### Run Tests
To run the test suite, execute:
```bash
python manage.py test
```

## Management Commands
- `send_overdue_notifications`: Sends email notifications to users with overdue books.
  ```bash
  python manage.py send_overdue_notifications
  ```

## License
This project is licensed under the MIT License.
