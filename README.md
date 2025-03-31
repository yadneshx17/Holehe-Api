# Holehe API

This is a FastAPI-based wrapper for the **Holehe** OSINT tool. It allows querying email addresses via an API instead of using the CLI.

## Installation

### Prerequisites
- Python 3.9+
- FastAPI
- Uvicorn
- Docker (Optional, for containerized deployment)

### Clone the Repository
```bash
git clone https://github.com/yourusername/holehe-api.git
cd holehe-api
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### API Key Setup
- Create a `.env` file in the project root:
  ```
  API_KEY=your-secret-api-key
  ```
- If `.env` is present, it will use this key. Otherwise, it defaults to `default-api-key`.

## Running the API
### Locally
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using Docker
#### Build and Run the Container
```bash
docker build -t holehe-api .
docker run -d -p 8000:8000 --env-file .env holehe-api
```

## API Usage
### Endpoint
```
GET /holehe/{email}
```

### Headers
```
X-API-Key: your-secret-api-key
```

### Example Request
```bash
curl -H "X-API-Key: your-secret-api-key" http://localhost:8000/holehe/test@example.com
```

### Example Response
```json
{
  "email": "test@example.com",
  "data": "{...response from holehe...}"
}
