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
  "name": "Sk",
  "email": "sk@gmail.com",
  "phone": "90909090"
}
```

### Real-Time Output on Frontend Page:

```
[CREATED] Sk - Sk@gmail.com
```

---

## ✅ WebSocket Frontend Page

Shows real-time messages like:

* `[CREATED] SK - sk@gmail.com`
* `[UPDATED] BB - bb@gmail.com`
* `[DELETED] Alok - alok@gmail.com`

---

## ⚠️ Notes

* This uses `InMemoryChannelLayer` — not recommended for production.
* For deployment, use Redis as the Channels backend for performance and scalability.
* Consider configuring Nginx + Daphne/Uvicorn + Redis for a full-stack production setup.

---
