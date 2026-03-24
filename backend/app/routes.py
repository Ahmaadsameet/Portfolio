from fastapi import APIRouter
from app.models import Task

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added", "task": task}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted"}