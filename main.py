from fastapi import FastAPI
from task import Task

app = FastAPI()
tasks = [
    Task(),
    Task()
]

@app.get("/")
def root():
    return "Hello World"

@app.get("/get-tasks")
def get_tasks():
    return tasks

@app.get("/task/(task_id)")
def get_task_by_id(task_id: int):
    found = True

@app.get("/get-task/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

@app.put("/{task_id}")
def update_task(task_id : int, updated: Task):
    for task in tasks:
        if task.id == task_id:
            task.description = updated.description
            task.is_complete = updated.is_complete
            return "Updated Task"
    return "Task Not Found"    
    
@app.post("/task")
def create_task(task : Task):
   tasks.append(task)
   return "Task Added"

@app.delete("/task//{task_id}")
def delete_task(task_id : int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return "Deleted Task"
    return "Task Not Found"