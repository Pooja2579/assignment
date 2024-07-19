Social Networking Application:

This is a social networking application built with Django and Django Rest Framework. It includes features such as user registration, login, user search, friend requests, and friend listing.

Features
User Registration and Authentication
Search for Users by Email or Name
Send, Accept, or Reject Friend Requests
List Friends
List Pending Friend Requests
Installation
Prerequisites
Python 3.6+
Django 3.2+
Django Rest Framework
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/social_network.git
cd social_network
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Apply the migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and go to:

arduino
Copy code
http://127.0.0.1:8000/
API Endpoints
User Registration
URL: /signup/

Method: POST

Headers: Content-Type: application/json

Body:

json
Copy code
{
    "email": "user@example.com",
    "name": "User Name",
    "password": "password123"
}
User Login
URL: /login/

Method: POST

Headers: Content-Type: application/json

Body:

json
Copy code
{
    "email": "user@example.com",
    "password": "password123"
}
Search Users
URL: /search/
Method: GET
Parameters: q (query string for email or name)
Send Friend Request
URL: /friend-request/<int:user_id>/
Method: POST
Handle Friend Request
URL: /friend-request/<int:request_id>/<str:action>/
Method: POST
Actions: accept, reject
List Friends
URL: /friends/
Method: GET
List Pending Friend Requests
URL: /friend-requests/pending/
Method: GET
Project Structure
markdown
Copy code
social_network/
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── social_network/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
└── requirements.txt
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or enhancements.
