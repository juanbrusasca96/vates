from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from db import engine, SessionLocal, Base, get_db
from sqlalchemy.orm import Session
from crud import get_users, create_user, get_user_by_email
from schema import UserOutput, UserCreate

app = FastAPI()
Base.metadata.create_all(bind=engine)


# db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/api/users', response_model=list[UserOutput])
async def get_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    users_request: list[UserOutput] = []
    for i in range(len(users)):
        users_request.append(UserOutput(
            email=users[i].email, is_active=users[i].is_active))
    return users_request


@app.post('/api/users', response_model=UserOutput)
async def create_user_request(user_request: UserCreate, db: Session = Depends(get_db)):
    user_email = get_user_by_email(db, user_request.email)
    if user_email:
        raise HTTPException(
            status_code=404, detail='el email ya esta registrado')
    user = create_user(db, user_request)
    user_request = UserOutput(email=user.email, is_active=user.is_active)
    return user_request
