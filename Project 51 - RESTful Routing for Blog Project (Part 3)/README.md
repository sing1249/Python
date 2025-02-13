# Flask Blog Application

A simple blog application built using Flask, SQLite, and Bootstrap. This project allows users to create, edit, and delete blog posts with a user-friendly interface.

## Features

- Create new blog posts with a title, subtitle, author name, image URL, and rich-text body.
- View all blog posts on the homepage.
- Click on individual posts to view their full content.
- Edit existing blog posts.
- Delete blog posts from the database.
- Uses Flask-WTF forms with validation.
- CKEditor integration for rich text editing.
- Bootstrap styling for a responsive design.

---

## Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy
- **Frontend:** Flask-Bootstrap, HTML, CSS
- **Database:** SQLite
- **Form Handling:** Flask-WTF, WTForms
- **Rich Text Editing:** Flask-CKEditor

---

## How It Works

### 1. Database Setup
- The app uses **SQLite** as its database.
- A `BlogPost` model is created with fields for `id`, `title`, `subtitle`, `date`, `body`, `author`, and `img_url`.
- `db.create_all()` ensures that the database tables are created before running the app.

### 2. Homepage (`/`)
- Displays all blog posts stored in the database.
- Uses `db.session.execute(db.select(BlogPost)).scalars().all()` to fetch all posts.
- The posts are then passed to the `index.html` template for rendering.

### 3. Viewing a Single Post (`/post/<int:post_id>`)
- When a user clicks on a blog post, they are taken to a detailed view of that post.
- The route fetches the post using `db.get_or_404(BlogPost, post_id)`.
- The `post.html` template is used to display the post.

### 4. Creating a New Post (`/new-post`)
- Uses **Flask-WTF forms** for user input validation.
- The **CKEditor** field allows rich-text editing.
- When a new post is submitted, the data is stored in the database, and the user is redirected to the homepage.

### 5. Editing a Post (`/edit-post/<int:post_id>`)
- Users can edit an existing blog post.
- The form is pre-filled with the existing data.
- Upon submission, the database entry is updated, and the user is redirected to the updated post.

### 6. Deleting a Post (`/delete/<int:post_id>`)
- Deletes a post from the database.
- Uses `db.get_or_404(BlogPost, post_id)` to fetch the post.
- Calls `db.session.delete(post_to_be_deleted)` followed by `db.session.commit()` to remove it.

### 7. About and Contact Pages (`/about`, `/contact`)
- These are static pages rendered with `about.html` and `contact.html`.

---
