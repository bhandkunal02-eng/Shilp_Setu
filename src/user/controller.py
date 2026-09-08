from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash


get_password_hash=PasswordHash()

def register(body:UserSchema,db:Session):
    ##1) user name Validation 
    is_user=db.query(UserModel).filter(UserModel.username==body.username).first()
    if is_user:
        raise HTTPException(400,detail="Username alreday exists")


# Email verification 

    is_user=db.query(UserModel).filter(UserModel.email==body.email).first
    if is_user:
        raise HTTPException(400,detail="Email  alreday exists")


    hash_password=get_password_hash(body.password)

    new_user=UserModel(
    name=body.name,
    username=body.username,
    hash_password=hash_password,
    email=body.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


