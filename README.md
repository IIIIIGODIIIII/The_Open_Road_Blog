# The Open Road Blog
This project is a blog website built using Django. The application allows users to register, log in, create and manage blog posts, and update their profiles.

## Features
1. User Authentication: Users can register, log in, and manage their profiles.
2. Blog Posts: Authenticated users can create, edit, and delete their blog posts.
3. Profile Management: Users can upload profile pictures.
4. Responsive Design: Uses Bootstrap for a mobile-friendly layout.
5. Password Reset: Users can reset their passwords via email.

## Technologies Used
1. Django: Backend framework for server-side logic.
2. Bootstrap: Frontend framework for responsive design.
3. SQLite: Default database for development.
4. HTML/CSS: For structuring and styling the web pages.

## Installation
To get a local copy up and running, follow these simple steps:

1. Clone the repository

   ```bash
   git clone https://github.com/IIIIIGODIIIII/The_Open_Road_Blog.git

2. Navigate to the project directory

   ```bash
   cd The_Open_Road_Blog

3. Apply migrations

   ```bash
   python manage.py migrate

4. Run deployment server

   ```bash
   python manage.py runserver

## Usage
1. Create a superuser
   ```bash
   python manage.py createsuperuser
   
2. Access the admin panel - Visit http://127.0.0.1:8000/admin/ to manage the blog content.

3. Navigate the website - Visit http://127.0.0.1:8000/ to explore the blog platform.
   
