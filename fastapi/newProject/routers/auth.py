from fastapi import APIRouter
from fastapi import Depends, HTTPException
from db import  get_db
from sqlalchemy.orm import Session
from crud import get_users, create_user, get_user_by_email, get_user_by_id, create_item_for_user
from schema import UserOutput, UserCreate, ItemCreate

router = APIRouter(
    prefix='/api/users',
    tags=['auth']
)

@router.get('/', response_model=list[UserOutput])
async def get_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    users_request: list[UserOutput] = []
    for i in range(len(users)):
        users_request.append(UserOutput(
            email=users[i].email, is_active=users[i].is_active))
    return users_request


@router.post('/', response_model=UserOutput)
async def create_user_request(user_request: UserCreate, db: Session = Depends(get_db)):
    user_email = get_user_by_email(db, user_request.email)
    if user_email:
        raise HTTPException(
            status_code=404, detail='el email ya esta registrado')
    user = create_user(db, user_request)
    user_request = UserOutput(email=user.email, is_active=user.is_active)
    return user_request


@router.get('/user_by_id/{user_id}', response_model=UserOutput)
async def get_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    user_request = UserOutput(email=user.email, is_active=user.is_active)
    return user_request