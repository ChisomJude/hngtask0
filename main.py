from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import pytz


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], 
)

timezone = pytz.timezone("Africa/Lagos")

@app.get("/")

def mygetapi():
    email = "chisomjude0205@gmail.com"
    current_datetime=(datetime.now()).isoformat()+ "Z"
    github_url ="https://github.com/ChisomJude/hngtask0"
    response = {
        "email": email,
        "current_datetime" : current_datetime,
        "github_url": github_url,
    }
    return response

