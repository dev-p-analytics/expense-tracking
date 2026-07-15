# Expense Management
This project is an expense management system that conists of Streamlit frontend application with a FastAPI backend server

## Project Structure
- **frontend/**: Contains the Streamlit application code
- **backend/**: Contains the FastAPI backend server code
- **tests/**: Contains the test cases for both frontend and backend
- **requirements.txt**: Lists the required python packages
- **README.md**: Provides an overview and instructions for the project

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/dev-p-analytics/expense-tracking
    cd expense-tracking
    ```
2. **Install Dependencies**:
    ```commandline
    pip install -r requirements.txt
    ```
3. **Run the FastAPI server**:
    ```commandline
    uvicorn server.server:app --reload
    ```
4. **Run the Streamlit app**:
    ```commandline
    streamlit run frontend/app.py
    ```
