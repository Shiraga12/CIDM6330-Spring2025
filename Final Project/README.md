# MRI Management System
A Django-based backend system designed to manage patients, schedule MRI appointments, generate invoices, and send notifications for a healthcare imaging center.

# Table of Contents
- Project Overview
- Features
- Architecture
- Installation
- API Endpoints
- Testing
- Repository Structure
- UML Diagrams
- License

# Project Overview
The MRI Management System streamlines healthcare imaging operations by:
- Managing patient records
- Scheduling, rescheduling, and canceling MRI appointments
- Generating invoices after appointments
- Sending notifications for reminders and billing alerts

# Features
- CRUD operations for patients, appointments, invoices, and notifications
- RESTful API design with Django REST Framework
- Automatic invoice generation upon appointment completion
- Email/SMS notifications sent for upcoming appointments and overdue payments
- Unit and BDD tests for major workflows

# Architecture
- Backend: Django + Django REST Framework
- Database: PostgreSQL (or default SQLite for development)
- Notifications: Email/SMS simulation (extendable to real services)
- Diagrams: UML diagrams located in /docs/diagrams/

# Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/mri-management.git
cd mri-management
```
2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Apply migrations
```bash
python manage.py migrate
```
5. Run the server
```bash
python manage.py runserver
```
# API Endpoints
| Method	| Endpoint              | Description                   |
|-----------|-----------------------|-------------------------------|
| GET	    | `/api/patients/`      | List all patients             |
| POST	    | `/api/patients/`      | Create a new patient          |
| GET	    | `/api/patients/{id}/`	| Retrieve patient details      |
| PUT	    | `/api/patients/{id}/`	| Update a patient              |
| DELETE	| `/api/patients/{id}/`	| Delete a patient              |
| GET	    | `/api/appointments/`  | List all appointments         |
| POST	    | `/api/appointments/`  | Schedule a new appointment    |   
| GET	    | `/api/invoices/`      | List all invoices             |
| POST	    | `/api/invoices/`      | Create an invoice             |
| GET	    | `/api/notifications/`	| List all notifications        |

_(More detailed API documentation coming soon via Swagger/OpenAPI)_

# Testing
Run all unit and BDD tests with:
```bash
python manage.py test
```
Tests are organized into:
- tests/test_patient.py
- tests/test_appointment.py
- tests/test_invoice.py
- tests/test_notification.py

# Repository Structure
```
Final Project/
├── MRI_App/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
│       ├── test_patient.py
│       ├── test_appointment.py
│       ├── test_invoice.py
│       └── test_notification.py
├── MRI_Management/
│   ├── settings.py
│   └── urls.py
├── docs/
│   └── diagrams/
├── requirements.txt
└── README.md
```
# UML Diagrams
Located under `/docs/diagrams/`:
- Use Case Diagram
- Activity Diagram
- Class Diagram
- Sequence Diagram
- Component Diagram
- State Machine Diagram

# License
This project is released under the MIT License.