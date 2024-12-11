# Expense Manager API

A Django-based RESTful API for managing user expenses. The project includes features such as CRUD operations for expenses, filtering expenses by date range, and summarizing expenses by category.

## Features
- Create, Read, Update, and Delete (CRUD) expenses.
- Filter expenses by a specific date range.
- Summarize total expenses by category for a given month.

---

## Prerequisites
- Python 3.8+ installed
- Pipenv or virtualenv for managing dependencies
- PostgreSQL (or other database as preferred)

---

## Setup Instructions

1. **Route to the repository:**
   ```bash
   cd expense_manager

2.	**Set up a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  
    # On Windows: env\Scripts\activate


3.	**Install dependencies:**
    ```bash
    pip install -r requirements.txt


4.	**Configure the database:**

•	Open expense_manager/settings.py and update the DATABASES setting with your database credentials.

5.	**Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate


6.	**Run the development server:**

    ```bash
    python manage.py runserver


7.	**Access the API:**

Open your browser and navigate to http://127.0.0.1:8000/api/.

---

API Endpoints

Expense CRUD Operations

Method	Endpoint	Description

**GET**	/api/expenses/	List all expenses

**POST**	/api/expenses/	Create a new expense

**GET**	/api/expenses/{id}/	Retrieve an expense by ID

**PUT**	/api/expenses/{id}/	Update an expense by ID

**DELETE**	/api/expenses/{id}/	Delete an expense by ID

List Expenses by Date Range
---
Method	Endpoint	Description

---

GET	/api/expenses/filter/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD	

---

List expenses within a date range

Category Summary

Method	Endpoint	Description

**GET**	/api/expenses/summary/?month=MM&year=YYYY	

Get total expenses per category for a given month

---

Validation Rules

•	Expense amount must be positive.

Future Enhancements

•	User authentication and authorization.

•	Advanced filtering and reporting.
