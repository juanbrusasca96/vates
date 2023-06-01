from sqlalchemy.orm import Session
from models import UserModel, ItemModel
from schema import UserCreate, ItemCreate


def get_users(db: Session):
    users_db = db.query(UserModel).all()
    return users_db


def get_user_by_id(db: Session, user_id: int):
    user_db = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user_db


def get_user_by_email(db: Session, user_email: str):
    user_db = db.query(UserModel).filter(UserModel.email == user_email).first()
    return user_db


def create_user(db: Session, user: UserCreate):
    fake_password = user.password + 'asd'
    db_user = UserModel(email=user.email, hashed_password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_items(db: Session):
    items_db = db.query(ItemModel).all()
    return items_db


def create_item_for_user(db: Session, item: ItemCreate, owner_id: int):
    # user_db = db.query(UserModel).filter(UserModel.id == owner_id).first()
    # item_db = ItemModel(
    #     title=item.title, description=item.description, owner_id=owner_id)
    item_db = ItemModel(**item.dict(), owner_id=owner_id)
    db.add(item_db)
    db.commit()
    db.refresh(item_db)
    return item_db
