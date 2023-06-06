from fastapi import APIRouter
from fastapi import Depends, HTTPException
from db import  get_db
from sqlalchemy.orm import Session
from crud import get_users, create_user, get_user_by_email, get_user_by_id, create_item_for_user
from schema import UserOutput, UserCreate, ItemCreate

router=APIRouter(
    prefix='/api/users',
    tags=['items']
)

@router.get('/get_items_by_user_id/{user_id}')
async def get_items_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    return user.items


@router.post('/{user_id}/item')
async def create_items(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    item_create = create_item_for_user(db, item, user_id)
    return item_create