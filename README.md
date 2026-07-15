# Expense Tracking System

A full-stack expense management application built with a FastAPI backend, MySQL database, and Streamlit frontend. Users can log daily expenses, view breakdowns by category, and analyse spending trends across months. Built as part of the Codebasics Data Engineering and Analytics course (Python optional project).

## Features

- Add, update, and delete expenses by date
- View expense breakdown by category with percentage share
- Analyse monthly spending trends across a selected date range
- Automated pytest test suite covering backend functions
- Clean REST API built with FastAPI

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI, Python 3.14 |
| Database | MySQL |
| Testing | Pytest |
| Other | Pandas, mysql-connector-python |

## Project Structure

```
expense-tracking/
├── backend/
│   ├── db_helper.py            # Database connection and query functions
│   └── server.py               # FastAPI endpoints
├── database/
│   └── expense_db_creation.sql # MySQL schema
├── frontend/
│   ├── app.py                  # Main Streamlit app
│   ├── analytics_ui.py         # Analytics by category tab
│   └── month_analytics_ui.py   # Analytics by month tab
├── tests/
│   ├── conftest.py             # Pytest path configuration
│   └── backend/
│       └── test_db_helper.py   # Backend unit tests
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/dev-p-analytics/expense-tracking
cd expense-tracking
```

### 2. Set up the MySQL database
Run the schema file in MySQL Workbench or terminal:
```sql
source database/expense_db_creation.sql
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI backend
```bash
cd backend
uvicorn server:app --reload
```

### 5. Run the Streamlit frontend
```bash
streamlit run frontend/app.py
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/expenses/{date}` | Fetch expenses for a specific date |
| POST | `/expenses/{date}` | Add or update expenses for a date |
| POST | `/analytics/` | Get category breakdown for a date range |
| GET | `/analytics/monthly` | Get monthly spending totals for a month range |

## Running Tests
```bash
pytest tests/ -v
```

## What I Learned

- Building a REST API with FastAPI and connecting it to a MySQL database
- Using Python context managers for safe and clean database connection handling
- Writing modular, reusable database helper functions
- Building an interactive frontend with Streamlit that consumes a REST API
- Writing automated pytest tests for database-backed functions
- Using os.path and __file__ for portable file paths across environments