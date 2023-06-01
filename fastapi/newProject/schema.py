from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: str


class Item(ItemCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserOutput(BaseModel):
    email: str
    is_active: bool


class UserCreate(UserOutput):
    password: str


class User(UserCreate):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
