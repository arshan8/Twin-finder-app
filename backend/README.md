# Resume Application Backend

This is the backend component of the Resume Application, built using FastAPI. It serves as the API layer for managing resumes and interacting with the Qdrant database.

## Project Structure

```
backend/
├── app/
│   ├── main.py               # Entry point for the FastAPI application
│   ├── api/
│   │   └── routes.py         # API routes for resume management
│   ├── models/
│   │   └── resume.py         # Data model for resumes
│   └── services/
│       └── qdrant_service.py # Service for interacting with Qdrant database
├── requirements.txt          # Python dependencies for the backend
└── README.md                 # Documentation for the backend
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd resume-app/backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application:**
   ```
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage Examples

- **Get all resumes:**
  ```
  GET /api/resumes
  ```

- **Add a new resume:**
  ```
  POST /api/resumes
  ```

- **Get a specific resume:**
  ```
  GET /api/resumes/{id}
  ```

Refer to the API documentation for more details on the available endpoints and their usage.