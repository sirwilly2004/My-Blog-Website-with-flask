**Flask Blog App**
This is a simple blog application built with Flask, SQLite, and Flask-WTF forms. The application allows users to create, edit, and display blog posts. It also includes features such as CKEditor for rich text formatting, sanitization with bleach for safe content input, and Bootstrap integration for a responsive UI.

**Features**

Home Page: Displays a list of blog posts with titles, subtitles, and authors.
Create New Post: Users can create new blog posts using a form that includes fields for title, subtitle, author, image URL, and blog content. CKEditor is used for the content field to allow rich text editing.
Edit Post: Existing blog posts can be edited. The content is sanitized using bleach to ensure that only safe HTML tags and attributes are allowed.
Responsive Design: The application is styled with Bootstrap for a modern, responsive layout.
Image Support: Posts can include an image, provided via an image URL field.
Post Dates: The date of each post is displayed in the format Month Day, Year (e.g., August 26, 2020).
Email Support: Users can send contact messages via email (configured with smtplib).

**Tech Stack**
**Flask:** A lightweight web framework for Python.
**SQLite:** Database to store blog post data.
**Flask-WTF**: For creating and handling forms.
**CKEditor: **Rich text editor used for the blog content field.
**Bleach**: A library for sanitizing HTML content to prevent XSS attacks.
**Bootstrap**: A front-end framework for responsive design.
**Flask-SQLAlchemy:** ORM for managing database interactions.
