# Flask Blog Application

## 📌 Overview
This is a fully functional blog application built with Flask. It allows users to register, log in, and interact with blog posts by commenting on them. Only the admin user can create, edit, and delete blog posts, ensuring control over the content. The app uses an SQLite database to store user information, blog posts, and comments.

## 🚀 Features

### 🔐 User Authentication & Management
- Users can **register** with their name, email, and password.
- Passwords are securely **hashed** using `pbkdf2:sha256` before storage.
- Users can **log in** and **log out** securely.
- If a user tries to register with an existing email, they are redirected to the login page with a flash message.

### 📝 Blog Post Management
- **View all posts** on the homepage.
- Click on any post to view the **full content**.
- **Only the admin (user ID = 1) can create, edit, or delete blog posts**.
- Posts contain:
  - Title
  - Subtitle
  - Author
  - Date of creation
  - Content (with CKEditor support for formatting)
  - Image URL

### 💬 Comments System
- Users can **leave comments** on posts.
- **Only logged-in users** can comment.
- Comments include:
  - The commenter's name and profile picture (via Gravatar).
  - The comment text.
- All comments are stored in the database and linked to both the user and the blog post.

### 🛡️ Role-Based Access Control
- **Admin-only actions**:
  - Creating new posts.
  - Editing existing posts.
  - Deleting posts.
- If a non-admin user tries to access these actions, they receive a **403 Forbidden error**.

## 🏗️ Technologies Used
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database management
- **Flask-Login** - User authentication
- **Flask-WTF** - Form handling
- **Flask-Bootstrap** - Styling
- **Flask-CKEditor** - Rich text editor for blog posts
- **Werkzeug Security** - Password hashing
- **Gravatar** - Profile images for users
- **SQLite** - Database
