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
    
#@app.get("/")
#def get_task():
 #   return "Hello World"

#@app.put("/")
#def get_task():
 #   return "Hello World"

#@app.post("/")
#def create_task():
 #   return "Hello World"

#@app.delete("/")
#def create_task():
    #return "Hello World"