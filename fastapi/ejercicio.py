from typing import Optional
from fastapi import FastAPI, Body, Path, Query
from enum import Enum

from pydantic import BaseModel, Field

app = FastAPI()


class Item:
    id: int
    name: str
    description: str
    price: float
    is_offer: bool

    def __init__(self, id, name, description, price, is_offer):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.is_offer = is_offer


class ItemRequest(BaseModel):
    id: Optional[int] = Field(title="El id no es necesario")
    name: str
    description: str
    price: float = Field(gt=0)
    is_offer: bool

    class Config:
        schema_extra = {
            "example": {
                "name": "Campera",
                "description": "Campera para el frio",
                "price": 25.22,
                "is_offer": True,
            }
        }


INITIAL_ITEMS = [
    Item(1, "Camiseta", "Camiseta de algodón para hombre", 25.99, False),
    Item(2, "Pantalón", "Pantalón de mezclilla para hombre", 45.99, True),
    Item(3, "Sudadera", "Sudadera con capucha para mujer", 35.99, True),
    Item(4, "Zapatos", "Zapatos de cuero para hombre", 65.99, False),
    Item(5, "Gorra", "Gorra con visera para mujer", 15.99, False),
    Item(6, "Mochila", "Mochila para excursiones", 50.99, True),
    Item(7, "Chamarra", "Chamarra de piel para hombre", 75.99, False),
    Item(8, "Bolsa", "Bolsa para laptop", 30.99, True),
    Item(9, "Reloj", "Reloj de pulsera para hombre", 55.99, False),
    Item(10, "Bufanda", "Bufanda de lana para mujer", 20.99, False),
    Item(11, "Playera", "Playera con estampado para hombre", 25.99, True),
    Item(12, "Jeans", "Jeans ajustados para mujer", 40.99, False),
    Item(13, "Botas", "Botas de invierno para hombre", 85.99, True),
    Item(14, "Gafas", "Gafas de sol para mujer", 18.99, False),
    Item(15, "Chaleco", "Chaleco acolchado para hombre", 60.99, True),
    Item(16, "Cinturón", "Cinturón de cuero para mujer", 22.99, False),
    Item(17, "Shorts", "Shorts de playa para hombre", 28.99, False),
    Item(18, "Vestido", "Vestido de fiesta para mujer", 80.99, True),
    Item(19, "Bolso", "Bolso de mano para mujer", 25.99, False),
    Item(20, "Zapatillas", "Zapatillas deportivas para hombre", 50.99, True),
]


class Offer(Enum):
    OFFER = "True"
    NO_OFFER = "False"


def validate_id(id: int):
    return id <= len(INITIAL_ITEMS)


def find_item_id(item: Item):
    item.id = 1 if len(INITIAL_ITEMS) == 0 else INITIAL_ITEMS[-1].id + 1
    return item


@app.get("/items")
def get_items():
    return INITIAL_ITEMS


@app.get("/items/{id}")
def get_item(id: int = Path(gt=0)):
    for item in INITIAL_ITEMS:
        if item.id == id:
            new_item = {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "is_offer": item.is_offer,
            }
            return new_item
    raise {"detail": "Item not found"}


@app.get("/items/filter_by_price/")
def get_item_by_price(item_price: int = Query(gt=0)):
    items_to_return = []
    for item in INITIAL_ITEMS:
        if item.price <= item_price:
            items_to_return.append(item)
    return {
        "items seleccionados": items_to_return,
        "porcentaje de items seleccionados": f"{len(items_to_return)* 100/ len(INITIAL_ITEMS)}%",
    }


@app.get("/items/filter_by_offer/")
def get_item_by_offer(is_offer: Offer):
    items_to_return = []
    for item in INITIAL_ITEMS:
        if str(item.is_offer) == is_offer.value:
            items_to_return.append(item)
    return {
        "items seleccionados": items_to_return,
        "porcentaje de items seleccionados": f"{len(items_to_return)* 100/ len(INITIAL_ITEMS)}%",
    }


@app.post("/items")
def add_item(item_request: ItemRequest):
    new_item = find_item_id(Item(**item_request.dict()))
    INITIAL_ITEMS.append(new_item)
    return {
        "mensaje": "El item ha sido agregado con exito",
        "item": new_item,
        "items": INITIAL_ITEMS,
    }


@app.put("/items/{id}")
def update_item(
    updated_item: ItemRequest,
    id: int = Path(gt=0),
):
    if validate_id(id):
        for i in range(len(INITIAL_ITEMS)):
            if INITIAL_ITEMS[i].id == id:
                new_item = Item(**updated_item.dict())
                new_item.id = id
                INITIAL_ITEMS[i] = new_item
                break
        return {
            "mensaje": "El item ha sido actualizado con exito",
            "item": new_item,
            "items": INITIAL_ITEMS,
        }
    else:
        return "El id no es correcto"


@app.delete("/items/{id}")
def delete_item(id: int = Path(gt=0)):
    if validate_id(id):
        for i in range(len(INITIAL_ITEMS)):
            if INITIAL_ITEMS[i].id == id:
                deleted_item = INITIAL_ITEMS[i]
                INITIAL_ITEMS.pop(i)
                break
        return {
            "mensaje": "El item ha sido eliminado con exito",
            "item": deleted_item,
            "items": INITIAL_ITEMS,
        }
    else:
        return "El id no es correcto"
