# Social Platform Django Project

## Overview

This is a simple social media platform built with Django. Users can sign up, log in, create posts (with optional images), like and comment on posts, follow/unfollow other users, and share posts. The project uses Django’s built-in authentication system and Bootstrap for basic styling.

## Features

- **User Authentication:** Sign up, log in, and log out.
- **Post Creation:** Users can create text posts and optionally upload images.
- **Like/Unlike Posts:** Users can like or unlike posts.
- **Commenting:** Users can comment on posts.
- **Follow/Unfollow:** Users can follow or unfollow other users.
- **Share Posts:** Users can share posts from others.
- **Feed:** Users see posts from themselves and users they follow.

## Project Structure

```
tweet/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── tweet/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd djangoProject
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install django
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Sign Up:** Go to `/signup/` to create a new account.
- **Log In/Out:** Use the login and logout links in the navigation.
- **Create Posts:** Use the form on the home page.
- **Like, Comment, Follow, Share:** Use the buttons under each post.
  

## Customization

- Templates are in `core/templates/core/`.
- Static files (CSS, JS, images) can be added as needed.
- Update models, forms, and views in the `core` app to extend functionality.

## License

This project is for educational purposes.
