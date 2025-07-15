# 📇 Contact Management System (Django + WebSocket)

A simple real-time contact management system built with **Django**, **Django REST Framework**, and **Django Channels**. It allows users to **create, update, and delete contacts** while receiving **real-time updates** via WebSocket — all without needing Redis.

---

## ✨ Features

- 🔧 Create, update, and delete contacts via REST API  
- 🔁 Real-time contact change broadcasts using WebSocket  
- 🧪 Simple frontend WebSocket UI (HTML + JavaScript)  
- ❌ No Redis required (uses `InMemoryChannelLayer` for development)

---

## 🚀 Tech Stack

- Python 3.10+  
- Django 5.2.4  
- Django REST Framework  
- Django Channels  
- Daphne (ASGI server)

---

## 📁 Project Structure

```

contact\_manager/
├── contacts/                  # Django app for managing contacts
│   ├── models.py             # Contact model
│   ├── views.py              # API views with WebSocket broadcast
│   ├── consumers.py          # Channels WebSocket consumer
│   ├── routing.py            # WebSocket URL routing
│   ├── templates/
│   │   └── contacts/
│   │       └── ws\_test.html  # WebSocket frontend page
├── contact\_manager/
│   ├── settings.py           # Django settings with Channels config
│   ├── urls.py               # Main URL routing
│   ├── asgi.py               # ASGI application setup
├── db.sqlite3                # SQLite database
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/contact-manager.git
cd contact-manager
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate        # On Windows: myvenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the ASGI Server with Daphne

```bash
daphne -b 127.0.0.1 -p 8000 contact_manager.asgi:application
```

---

## 🌐 Access the WebSocket Frontend

Open your browser to:

```
http://127.0.0.1:8000/api/ws-test/
```

---

## 📬 Example API Usage (via Thunder Client / Postman)

### Create Contact (POST)

```
POST http://127.0.0.1:8000/api/contacts/
Content-Type: application/json
```

#### Request Body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}
```

### Real-Time Output on Frontend Page:

```
[CREATED] John Doe - john@example.com
```

---

## ✅ WebSocket Frontend Page

Shows real-time messages like:

* `[CREATED] John Doe - john@example.com`
* `[UPDATED] Jane Smith - jane@example.com`
* `[DELETED] Alice - alice@example.com`

---

## ⚠️ Notes

* This uses `InMemoryChannelLayer` — not recommended for production.
* For deployment, use Redis as the Channels backend for performance and scalability.
* Consider configuring Nginx + Daphne/Uvicorn + Redis for a full-stack production setup.

---

## 📄 License

MIT License

---

> Need Docker or Redis support? Let me know, and I’ll help you extend this setup for production.

```

---

Let me know if you want me to:

- Add Docker setup instructions  
- Switch to Redis-based channel layer for production  
- Add authentication or login system  
- Package this as an installable app or deployable project (Heroku/Vercel/etc.)

I'm happy to help!
```
