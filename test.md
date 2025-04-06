# Testing the Alx Library Management System Using a Browser

This document provides a step-by-step guide to test the functionalities of the Alx Library Management System using a browser.

---

## 1. User Registration
### Steps:
1. Open your browser and navigate to `http://127.0.0.1:8000/register/`.
2. Fill in the registration form with the following details:
   - **Username**: Enter a unique username.
   - **Email**: Enter a valid email address.
   - **Password**: Enter a strong password.
   - **Confirm Password**: Re-enter the password.
3. Click the "Register" button.
4. Verify that you are redirected to the login page and see a success message.

---

## 2. User Login
### Steps:
1. Navigate to `http://127.0.0.1:8000/login/`.
2. Enter your registered username and password.
3. Click the "Login" button.
4. Verify that you are redirected to the homepage or dashboard.

---

## 3. View Books
### Steps:
1. Navigate to `http://127.0.0.1:8000/books/list/`.
2. Verify that a list of books is displayed.
3. Use the search bar to filter books by title, author, or ISBN.
4. Check the "Show only available books" checkbox to filter available books.

---

## 4. Book Details
### Steps:
1. Click on a book title or the "View Details" button from the book list.
2. Verify that the book details page is displayed, showing the title, author, ISBN, published date, and available copies.
3. If copies are available, click the "Check Out" button.
4. Verify that the book is checked out and the available copies are decremented.

---

## 5. Borrowing History
### Steps:
1. Navigate to `http://127.0.0.1:8000/borrowing-history/`.
2. Verify that a table of borrowing transactions is displayed.
3. Check the "Return" button for books that have not been returned.
4. Click the "Return" button and verify that the return date is updated.

---

## 6. Profile Update
### Steps:
1. Navigate to `http://127.0.0.1:8000/profile/`.
2. Click the "Edit Profile" button.
3. Update your profile details and click "Save".
4. Verify that the changes are reflected on the profile page.

---

## 7. Admin Dashboard
### Steps:
1. Log in as an admin user.
2. Navigate to `http://127.0.0.1:8000/admin-dashboard/`.
3. Verify that the dashboard displays statistics for books, users, and transactions.

---

## Notes
- Ensure the development server is running by executing `python manage.py runserver`.
- Use different browsers or incognito mode to test multiple user sessions.
- Report any issues or unexpected behavior for debugging.