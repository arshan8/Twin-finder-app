# Frontend README for Resume App

# Resume App Frontend

This is the frontend component of the Resume App, built using Streamlit. The frontend interacts with the FastAPI backend to display and manage resumes.

## Installation

To set up the frontend, ensure you have Python installed. Then, install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Components

- **app.py**: The main entry point for the Streamlit application. It initializes the app and defines the layout.
- **components/resume_viewer.py**: Contains components for rendering resumes in a user-friendly format.

## Usage

Once the application is running, you can view and interact with resumes. The frontend communicates with the backend to fetch and display resume data.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.