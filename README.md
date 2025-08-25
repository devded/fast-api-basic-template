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

```
python main.py
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Welcome message
- `GET /core/health` - Health check endpoint (includes Redis connection test)
- `GET /core/info` - Application information
- `POST /core/insert` - Inserts a document into the vector database.
- `GET /core/search` - Searches for documents in the vector database.


- `POST /job/add` - Adds a new job description to the vector database.
- `GET /job/search` - Searches for jobs in the vector database.
- `POST /user/add` - Adds a new user.

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc