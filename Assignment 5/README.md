# Django REST API - Assignment 4

## 📌 Project Overview
This project is a migration of our FastAPI-based API to **Django REST Framework (DRF)**. It provides CRUD operations for managing **patients, appointments, and notifications** using Django’s built-in ORM.

## 🏗 Features
- RESTful API for **patients, appointments, and notifications**
- **Django ORM** for database management
- API endpoints with **Django REST Framework (DRF)**
- Browsable API Interface
- Uses **SQLite/PostgreSQL** (configurable)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/CIDM6330-Spring2025.git
cd CIDM6330-Spring2025/Assignment4
```

### 2️⃣ Create & Activate Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```bash
python manage.py makemigrations myapi
python manage.py migrate
```

### 5️⃣ Create a Superuser (For Admin Panel)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔗 API Endpoints

| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/api/patients/`        | Get all patients |
| GET    | `/api/patients/{id}/`   | Get a patient by ID |
| POST   | `/api/patients/`        | Create a new patient |
| PUT    | `/api/patients/{id}/`   | Update a patient |
| DELETE | `/api/patients/{id}/`   | Delete a patient |
| GET    | `/api/appointments/`    | Get all appointments |
| POST   | `/api/appointments/`    | Create an appointment |
| GET    | `/api/notifications/`   | Get all notifications |

---

## 🛠 Tech Stack
- **Django** (Backend Framework)
- **Django REST Framework** (API)
- **SQLite/PostgreSQL** (Database)
- **Docker** (Optional)
- **GitHub** (Version Control)

---

## 🤝 Contributing
Feel free to fork this repo and contribute! Create a new branch and submit a pull request.

---

## 📜 License
This project is licensed under the MIT License.
