from typing import Annotated, Optional, Union
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

# Crear una clase item con los siguientes campos: nombre, descripcion, precio, impuestos
# descripcion e impuestos opcional, nombre tipo str y precio tipo float
# endpoint de tipo put que recibe un path param de tipo int que sea mayor que 0 y menor o igual a 1000, ademas va a recibir un query param de tipo str y un item de tipo item (crear clase Item)


class Usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int


class Item(BaseModel):
    nombre: str
    # descripcion: Union[str, None]=None
    descripcion: Annotated[str, None] = None
    # descripcion: str | None = None
    precio: float
    # impuestos: float | None = None
    impuestos: Annotated[str, None] = None
    etiqueta: set[str] = set()
    usuarios: list[Usuario]=[]

    # def __init__(self, nombre, descripcion, precio, impuestos):
    #     self.nombre=nombre
    #     self.descripcion=descripcion
    #     self.precio=precio
    #     self.impuestos=impuestos




@app.put('/item/{item_id}')
# def update_item(item_id: int = Path(gt=0, le=1000)):
# q: Optional[str], item: Union[Item, None] = None , dos maneras de poner un parametro como opcional, no es recomendado trabajar on Optional en fastapi, se una mas Union. Annotated es mas nuevo
def update_item(item_id: Annotated[int, Path(gt=0, le=1000)], q: Union[str, None] = None, item: Union[Item, None] = None, usuario: Union[Usuario, None] = None, importancia: int = Body()):
    resultado = {
        "item_id": item_id
    }
    if q:
        resultado.update({'q': q})
    if item:
        resultado.update({'item': item})
    if usuario:
        resultado.update({'usuario': usuario})
    return resultado
