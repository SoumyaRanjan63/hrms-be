# HRMS Lite – Backend

## Project Overview

This project is the backend service for HRMS Lite, a lightweight Human Resource Management System that allows an admin to manage employee records and track daily attendance.

The backend provides RESTful APIs to:

* Add, list, and delete employees
* Mark attendance for employees
* View attendance records per employee

The system uses PostgreSQL for data persistence and Django REST Framework for API development.

---

## Tech Stack Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Gunicorn (for deployment)

---

## Steps to Run the Project Locally

### 1. Clone the repository

```bash
git clone <https://github.com/SoumyaRanjan63/hrms-be>
cd hrms-be
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=hrms
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

Backend will be available at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Employee

* `POST /api/employees/` – Add employee
* `GET /api/employees/` – List employees
* `DELETE /api/employees/{id}/` – Delete employee

### Attendance

* `POST /api/attendance/` – Mark attendance
* `GET /api/attendance/` – List all attendance

---

## Assumptions / Limitations

* Single admin user; authentication is not implemented.
* Attendance is recorded once per employee per date.
* Employee deletion is restricted if attendance records exist.
