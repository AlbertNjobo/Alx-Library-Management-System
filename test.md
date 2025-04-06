# Testing the Alx Library Management System with Postman

This document provides a step-by-step guide to test the functionalities of the Alx Library Management System using Postman.

---

## 1. User Registration
### Endpoint
**POST** `/register/`

### Request Body (JSON)
```json
{
  "username": "test_user",
  "password": "password123",
  "email": "test_user@example.com"
}
```

### Expected Response
- **201 Created**: User is successfully registered.

---

## 2. User Login
### Endpoint
**POST** `/login/`

### Request Body (JSON)
```json
{
  "username": "test_user",
  "password": "password123"
}
```

### Expected Response
- **200 OK**: User is successfully logged in, and a session cookie is returned.

---

## 3. View Books
### Endpoint
**GET** `/books/list/`

### Expected Response
- **200 OK**: A list of books is returned.

---

## 4. Search Books
### Endpoint
**GET** `/books/list/?q=<search_query>`

### Example
**GET** `/books/list/?q=Test`

### Expected Response
- **200 OK**: A filtered list of books matching the search query is returned.

---

## 5. Borrow a Book (Check-Out)
### Endpoint
**POST** `/books/<book_id>/checkout/`

### Expected Response
- **200 OK**: The book is successfully checked out, and the available copies are decremented.

---

## 6. View Borrowing History
### Endpoint
**GET** `/borrowing-history/`

### Expected Response
- **200 OK**: A list of borrowing transactions for the logged-in user is returned.

---

## 7. Return a Book
### Endpoint
**POST** `/transactions/<transaction_id>/return/`

### Expected Response
- **200 OK**: The book is successfully returned, and the available copies are incremented.

---

## 8. Admin Dashboard
### Endpoint
**GET** `/admin-dashboard/`

### Expected Response
- **200 OK**: An overview of books, users, and transactions is returned.

---

## 9. View Transactions (Admin Only)
### Endpoint
**GET** `/transactions/`

### Expected Response
- **200 OK**: A list of all transactions is returned.

---

## 10. Send Overdue Notifications
### Command
Run the following command in the terminal:
```bash
python manage.py send_overdue_notifications
```

### Expected Outcome
- Email notifications are sent to users with overdue books.

---

## Notes
- Ensure that you are logged in before testing endpoints that require authentication.
- Use the session cookie returned during login for subsequent requests.
- Replace `<book_id>` and `<transaction_id>` with actual IDs from your database.