from pydantic import BaseModel


class UserOutput(BaseModel):
    email: str
    is_active: bool


class UserCreate(UserOutput):
    password: str


class User(UserCreate):
    id: int
    items: list

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    title: str
    description: str
    owner_id: int


class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
