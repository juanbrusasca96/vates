from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from db import engine, SessionLocal, Base, get_db
from sqlalchemy.orm import Session
from crud import get_users, create_user, get_user_by_email, get_user_by_id, create_item_for_user
from schema import UserOutput, UserCreate, ItemCreate
from routers import auth, items

app = FastAPI()
Base.metadata.create_all(bind=engine)


# db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(auth.router)
app.include_router(items.router)

