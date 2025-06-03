# Qdrant Database Setup and Usage

This document provides instructions for setting up and using the Qdrant database within the resume application project.

## Overview

Qdrant is a vector similarity search engine that allows for efficient storage and retrieval of high-dimensional data. In this project, we utilize Qdrant to manage and query resume data.

## Installation

To use Qdrant, ensure you have Docker installed on your machine. You can run Qdrant using the following command:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

This command will start the Qdrant server, making it accessible at `http://localhost:6333`.

## Configuration

Before running the application, you may need to configure the connection settings in the `qdrant_service.py` file located in the `backend/app/services` directory. Ensure that the Qdrant client is properly set up to connect to your Qdrant instance.

## Usage

The Qdrant database is used in the application to perform the following operations:

- **Add Resume**: Store a new resume in the database.
- **Retrieve Resumes**: Fetch resumes based on specific queries.
- **Manage Resumes**: Update or delete existing resumes.

Refer to the `qdrant_service.py` file for detailed function definitions and usage examples.

## Additional Resources

For more information on Qdrant, visit the official documentation at [Qdrant Documentation](https://qdrant.tech/documentation/).