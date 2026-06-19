from fastapi import FastAPI, HTTPException #HTTPException es para capturar errors
from pydantic import BaseModel #Biblioteca para definir modelos de datos

mi_app= FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

class Factura(BaseModel): 
    id: int 
    cliente_id: int 
    vrtotal: float
    
class Transaccion(BaseModel): 
    id: int 
    vr_unitario: float 
    cantidad: int 
    factura_id: int



lista_clientes:list[Cliente] = [
    {"id": 1, "nombre": "Lady", "email": "lady@gmail.com", "edad": 22, "descripcion": "NA"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "edad": 19, "descripcion": "NA"},
    {"id": 3, "nombre": "Ana", "email": "ana@gmail.com", "edad": 23, "descripcion": "NA"},
    {"id": 4, "nombre": "Carlos", "email": "carlos@gmail.com", "edad": 25, "descripcion": "NA"},
    {"id": 5, "nombre": "Sofía", "email": "sofia@gmail.com", "edad": 21, "descripcion": "NA"},
]

#endpoint listar todos los clientes
@mi_app.get("/clientes")
def listar_clientes():
     return lista_clientes

#endpoint listar un cliente
@mi_app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    for i, obj_client in enumerate(lista_clientes):
        if obj_client.get("id") == cliente_id:
            return obj_client
        
#endpoint para crear clientes y agregar a la lista
@mi_app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente
    
     
