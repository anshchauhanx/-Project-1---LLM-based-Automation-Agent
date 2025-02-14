from fastapi import FastAPI, Query, HTTPException
from dotenv import load_dotenv
import os
from app.tasks import execute_task

# Load environment variables
load_dotenv()

app = FastAPI()

@app.post("/run")
def run_task(task: str = Query(..., description="Task description")):
    """Executes the given task"""
    try:
        result = execute_task(task)
        return {"message": "Task executed successfully", "output": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Task not recognized")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
def read_file(path: str):
    """Returns the content of a specified file."""
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
