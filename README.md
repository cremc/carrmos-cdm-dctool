# Qued Data Collection Tool

## Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **MySQL Server**

## Setup & Running

### 1. Database Setup
1.  Open your MySQL client (e.g., MySQL Workbench).
2.  Create the database:
    ```sql
    CREATE DATABASE qued_india_initial;
    ```
3.  Configure the connection string in `server/app/database.py`. Update the `user:password` part with your MySQL credentials.
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://<USER>:<PASSWORD>@localhost/qued_india_initial"
    ```

### 2. Backend (Server)
1.  Open a terminal in the `server` directory.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.
    Swagger UI documentation will be at `http://localhost:8000/docs`.

### 3. Frontend (Client)
1.  Open a **new** terminal in the `client` directory.
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Run the development server:
    ```bash
    npm run dev
    ```
    The application will be available at `http://localhost:5173`.
