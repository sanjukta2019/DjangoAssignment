🔐 Django REST User Authentication & Management API

This project is a Django REST Framework–based backend API that provides custom user management, authentication, password change, and password reset functionality.
It is designed as a RESTful backend service suitable for integration with frontend applications (React, Angular, mobile apps, etc.).

🚀 Features

Custom User Model (AbstractUser)

User listing API

Change password API

Password reset via email token

REST authentication (login/logout)

Token-based authentication

Django Admin integration

SQLite database (development)

Modular app structure (users, api)

🛠️ Tech Stack

Python 3

Django 3.1.1

Django REST Framework

django-rest-auth

django-allauth

django-rest-passwordreset

SQLite

📂 Project Structure
projectdrfx/
│
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── projectdrfx/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md

👤 Custom User Model

The project uses a custom user model defined in users/models.py:

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phonenumber = models.CharField(max_length=10, blank=True)


Configured in settings.py:

AUTH_USER_MODEL = 'users.CustomUser'

🌐 API Endpoints
🔹 User APIs
Endpoint	Method	Description
/api/v1/users/	GET	List all users
/api/v1/users/change-password	PUT	Change user password
🔹 Authentication APIs
Endpoint	Method	Description
/api/v1/rest-auth/login/	POST	Login
/api/v1/rest-auth/logout/	POST	Logout
/api/v1/rest-auth/registration/	POST	Register new user
🔹 Password Reset APIs
Endpoint	Method	Description
/api/v1/password_reset/	POST	Request password reset
/api/v1/reset-password/confirm/	POST	Confirm password reset

📧 Password reset emails are sent using Django’s console email backend (for development).

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone <repository-url>
cd projectdrfx

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies
pip install django==3.1.1
pip install djangorestframework
pip install django-rest-auth
pip install django-allauth
pip install django-rest-passwordreset

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run the Development Server
python manage.py runserver

7️⃣ Open in Browser / API Client
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/v1/

🔐 Permissions & Security

Password change endpoint requires authentication

Token authentication supported

Passwords are securely hashed using Django’s auth system

🧪 Testing

Run tests using:

python manage.py test

🔮 Future Enhancements

JWT authentication

Swagger / OpenAPI documentation

Role-based access control

Email backend integration (SMTP)

PostgreSQL database

Docker support

👩‍💻 Author

Sanjukta Bag
