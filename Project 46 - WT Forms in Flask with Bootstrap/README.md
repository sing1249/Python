# Flask Login Application

A simple Flask web application demonstrating user authentication with `WTForms`, form validation, and Bootstrap 5 templates.

## Features

- **WTForms**: Handles form fields like `email` and `password`, including built-in validation for `DataRequired`, `Email`, and `Length`.
- **Flask-Bootstrap**: Integrates Bootstrap 5 for responsive, modern UI styling.
- **Template Inheritance**: Uses `base.html` for a consistent layout, allowing other templates like `login.html` to extend and customize it.
- **Form Validation**: The login form ensures valid email and password inputs before checking the credentials.

## Templates

- **base.html**: The base layout template, providing the structure and loading Bootstrap 5 CSS.
- **login.html**: Displays the login form, extending `base.html` for a consistent layout.
- **success.html**: Shows after a successful login.
- **denied.html**: Shows when login credentials are incorrect.
