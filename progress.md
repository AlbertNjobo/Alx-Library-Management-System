# Library Management System API Progress

## Project Overview
The Library Management System API is being developed for the Institute of Chartered Accountants of Zimbabwe (ICAZ). The API will manage library resources, allowing users to borrow, return, and view books. The main color theme is `#2e3192`, and the font is `Poppins`.

## Completed Steps

### Step 1: Set Up the Project
- Django project and app (`books`) have been set up.
- Django REST Framework (DRF) is installed and configured.

### Step 2: Define Models
- Created models for:
  - **Book**: Attributes: Title, Author, ISBN, Published Date, Number of Copies Available.
  - **LibraryUser**: Attributes: Username, Email, Date of Membership, Active Status.
  - **Transaction**: Attributes: User, Book, Check-Out Date, Return Date.
- Applied migrations to update the database schema.

### Step 3: Create Serializers
- Defined serializers for:
  - **Book**
  - **LibraryUser**
  - **Transaction**

### Step 4: Implement CRUD for Books
- Added a `BookViewSet` to handle CRUD operations for books.
- Configured URLs to expose `/books/` endpoint using DRF's router.

### Step 5: Authentication Setup
- Configured Django REST Framework to use session and basic authentication.
- Set the default permission to `IsAuthenticated`.
- Created a superuser for testing authentication.

### Testing the API
- The server is running, and the `/books/` endpoint is accessible.
- Example requests for testing CRUD operations have been provided, including:
  - Adding a new book (POST `/books/`)
  - Retrieving all books (GET `/books/`)
  - Updating a book (PUT `/books/{id}/`)
  - Deleting a book (DELETE `/books/{id}/`)

## Next Steps
- Implement CRUD for users.
- Add endpoints for checking out and returning books.
- Implement filtering and searching for books.
- Deploy the API to a hosting platform.