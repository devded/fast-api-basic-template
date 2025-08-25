# SimpleAPI

A simple FastAPI application with core and subscription functionality for Basic.

## Features

- Core application information and health check
- Simple and clean API structure
- Vector database integration with Qdrant for document storage and search

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Copy the environment variables file and configure it:
   ```
   cp .env.example .env
   ```
- `QDRANT_HOST`: Host for Qdrant (default: `localhost`)
- `QDRANT_PORT`: Port for Qdrant (default: `6333`)

### Configuration

All Redis and Qdrant configurations are now centralized in `app/config.py` for easier management and modularity.

## Running the Application

### Locally
To run the application, execute the `main.py` file:

```bash
python main.py
```

### Using Docker
To build the Docker image:

```bash
docker build -t fastapi-basic .
```

To run the Docker container:

```bash
docker run -p 8000:8000 fastapi-basic
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Welcome message
- `GET /core/health` - Health check endpoint (includes Redis connection test)
- `GET /core/info` - Application information
- `POST /core/insert` - Inserts a document into the vector database.
- `GET /core/search` - Searches for documents in the vector database.


### Job Application APIs

-   `POST /job/add`
    -   **Method**: `POST`
    -   **Endpoint**: `/job/add`
    -   **Description**: Adds a new job description to the vector database.
    -   **Request Body**: `{"description": "string"}`

-   `GET /job/search`
    -   **Method**: `GET`
    -   **Endpoint**: `/job/search`
    -   **Description**: Searches for jobs in the vector database based on a query.
    -   **Query Parameters**: `query` (string, required), `limit` (integer, optional, default: 3)

-   `GET /job/recommendation`
    -   **Method**: `GET`
    -   **Endpoint**: `/job/recommendation`
    -   **Description**: Provides job recommendations for a given user ID.
    -   **Query Parameters**: `user_id` (string, required)

### User Application APIs

-   `POST /user/add`
    -   **Method**: `POST`
    -   **Endpoint**: `/user/add`
    -   **Description**: Adds a new user to the system. Requires `X-API-Key` header for authorization.
    -   **Request Body**: (Depends on your user model, e.g., `{"username": "string", "email": "string"}`)
    -   **Headers**: `X-API-Key` (string, required)


## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc