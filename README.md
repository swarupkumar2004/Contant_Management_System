# Contant_Management_System
📇 Contact Management System (Django + WebSocket)
This is a simple real-time contact management system built with Django, Django REST Framework, and Django Channels. It allows users to create, update, and delete contacts and view real-time updates through WebSocket.

✨ Features
Create, update, and delete contacts via REST API

Real-time broadcast of contact changes via WebSocket

Frontend WebSocket test UI (HTML + JavaScript)

No Redis required (uses InMemoryChannelLayer)

🚀 Tech Stack
Python 3.10+

Django 5.2.4

Django REST Framework

Django Channels

Daphne ASGI server

📁 Project Structure
contact_manager/
├── contacts/ # Django app for managing contacts
│ ├── models.py # Contact model
│ ├── views.py # API views with WebSocket broadcast
│ ├── consumers.py # Channels WebSocket consumer
│ ├── routing.py # WebSocket URL routing
│ ├── templates/
│ │ └── contacts/
│ │ └── ws_test.html # WebSocket frontend
├── contact_manager/
│ ├── settings.py # Django settings (ASGI + Channels config)
│ ├── urls.py # Django URL routing
│ ├── asgi.py # ASGI application setup
├── db.sqlite3 # SQLite database
├── requirements.txt
└── README.md

⚙️ Installation
Clone the repository:

git clone https://github.com/yourusername/contact-manager.git
cd contact-manager

Create and activate a virtual environment:

python -m venv myvenv
source myvenv/bin/activate # On Windows: myvenv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the ASGI server:

daphne -b 127.0.0.1 -p 8000 contact_manager.asgi:application

Access the frontend WebSocket test page:

Open browser to:
http://127.0.0.1:8000/api/ws-test/

Use Thunder Client / Postman to POST/PUT/DELETE:

POST http://127.0.0.1:8000/api/contacts/
Content-Type: application/json

{
"name": "John Doe",
"email": "john@example.com",
"phone": "1234567890"
}

Each change will appear live on the frontend.

✅ WebSocket Frontend Page
Displays real-time updates like:
[CREATED] John Doe - john@example.com

⚠️ Notes
This uses Django's InMemoryChannelLayer (not production ready).

To scale this for production, use Redis as the channel layer backend.

📄 License
MIT License
