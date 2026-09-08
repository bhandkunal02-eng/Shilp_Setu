from fastapi import APIRouter,Depends,status
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db


task_routes=APIRouter(prefix="/tasks")

@task_routes.post("/create",status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db=Depends(get_db)):
    return controller.create_task(body,db)



@task_routes.get("/all_tasks",status_code=status.HTTP_200_OK)
def get_all_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/one_task/{task_id}",status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db=Depends(get_db)):
    return controller.get_one_task(task_id,db)


@task_routes.put("/update_task/{task_id}",status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema,task_id:int,db=Depends(get_db)):
    return controller.update_task(body,task_id,db)

@task_routes.delete("/delete/{task_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_task(task_id:int,db=Depends(get_db)):
    return controller.delete_task(task_id,db)
