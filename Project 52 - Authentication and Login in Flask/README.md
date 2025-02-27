# Flask Authentication System

## Overview
This is a Flask-based authentication system that includes user registration, login, logout, and access to protected routes. The project utilizes Flask, Flask-Login for user authentication, Flask-SQLAlchemy for database management, and Werkzeug for password hashing.

## Features
- User registration with hashed passwords  
- User login with session management  
- Protected routes requiring authentication  
- User logout functionality  
- Downloading protected files for authenticated users  
- Flash messages for better user experience  

## Technologies Used
- Python  
- Flask  
- Flask-Login  
- Flask-SQLAlchemy  
- Werkzeug Security  
- SQLite  

## Project Structure
```
flask-authentication-system/
│── static/
│   ├── files/
│   │   ├── cheat_sheet.pdf
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── secrets.html
│── app.py
│── requirements.txt
│── users.db (generated at runtime)
│── README.md
```

