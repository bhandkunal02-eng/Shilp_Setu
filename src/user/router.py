from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserSchema
from src.user import controller



user_routes=APIRouter(prefix="/users")

@user_routes.post("/register",status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controller.register(body,db)
