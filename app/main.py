from fastapi import FastAPI, HTTPException
from app.tasks import execute_task
from app.llm import parse_task  # LLM-based task interpreter
import traceback
import os
from dotenv import load_dotenv

# Load environment variables (API Key)
load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")

# Initialize FastAPI
app = FastAPI(title="LLM Automation API", description="Automates tasks using LLM", version="1.0")

@app.get("/")
def home():
    """Welcome message on the root route"""
    return {"message": "Welcome to the LLM Automation API! Visit /docs for API documentation."}

@app.post("/run")
def run_task(task: str):
    """
    Executes a given task.
    - If successful, returns 200 OK
    - If the task is invalid, returns 400 Bad Request
    - If an internal error occurs, returns 500 Internal Server Error
    """
    try:
        structured_task = parse_task(task)  # LLM-based parsing
        result = execute_task(structured_task)
        return {"message": "Task executed successfully", "output": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print("🔥 ERROR TRACEBACK 🔥\n", traceback.format_exc())  # Log full error
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/read")
def read_file(path: str):
    """
    Reads a file from the /data directory.
    - Returns 200 OK if successful
    - Returns 403 Forbidden if accessing outside /data
    - Returns 404 Not Found if the file does not exist
    """
    try:
        if not path.startswith("data/"):
            raise HTTPException(status_code=403, detail="Access denied")
        with open(path, "r") as file:
            return {"content": file.read()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        print("🔥 ERROR TRACEBACK 🔥\n", traceback.format_exc())  # Log full error
        raise HTTPException(status_code=500, detail="Internal Server Error")
