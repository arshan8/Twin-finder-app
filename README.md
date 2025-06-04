# TWIN finding web app!!

This project utilizes FastAPI for the backend, Streamlit for the frontend, and Qdrant as the database for storing and managing resume data.

## Project Structure

```
resume-app
├── backend
│   ├── app
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   ├── api
│   │   │   └── routes.py    
│   │   ├── models
│   │   │   └── resume.py    
│   │   └── services
│   │       └── qdrant_service.py # Service for interacting with Qdrant database
│   ├── requirements.txt      # Backend dependencies #HOW ABOUY HAVING IT IN ROOT DIRECTORY??
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── app.py                # Entry point for the Streamlit application
│   ├── requirements.txt       # Frontend dependencies #LETS MERGE IT WITH GLOBAL DEPENDENCIES ONLY
│   └── README.md              # Documentation for the frontend
├── qdrant
│   └── README.md              # Documentation for Qdrant setup and usage
└── README.md                  # Overview of the entire project
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Backend Setup  BUT I STRONGLY RECOMMEND USING VENV OR POETRY SHELL OR UV

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

## Usage

- Access the FastAPI documentation at `http://localhost:8000/docs` to explore the available API endpoints.
- Use the Streamlit application to view and manage resumes.

## Qdrant Database

Refer to the `qdrant/README.md` for instructions on setting up and using the Qdrant database.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

