import subprocess
import json
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
    
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production (e.g., ["https://yourfrontend.com"])
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# API Key Setup
API_KEY = os.getenv("API_KEY", "default-api-key")  # Fallback in case .env is missing
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Function to check API key
def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/holehe/{email}")
def run_holehe(email: str, api_key: str = Depends(get_api_key)):
    try:
        # Runs Holehe tool
        result = subprocess.run(
            ["holehe", email],
            # ["holehe", "--only-used", email],
            capture_output=True, text=True
        )

        output = result.stdout.strip()
        return {"email": email, "data": output}
    
    except Exception as e:
        return {"error": str(e)}

# API without authentication.
"""
@app.get("/holehe/{email}")
def run_holehe(email: str):
    try:
        result = subprocess.run(
            ["holehe", "--only-used", email],  
            capture_output=True, text=True
        )
        output = result.stdout.strip()
        return {"email": email, "data": output}
    
    except Exception as e:
        return {"error": str(e)}
"""