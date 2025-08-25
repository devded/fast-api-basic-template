# SimpleAPI

A simple FastAPI application with core and subscription functionality for Basic.

## Features

- Core application information and health check
- Simple and clean API structure

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
   Then edit the `.env` file with your API keys, including BDApps subscription credentials if needed.

## Running the Application

```
python main.py
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Welcome message
- `GET /core/health` - Health check endpoint
- `GET /core/info` - Application information
- `GET /subscription/hello` - Returns a "Hello World!" message

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc