from fastapi import FastAPI, HTTPException #HTTPException es para capturar errors
from pydantic import BaseModel #Biblioteca para definir modelos de datos

mi_app= FastAPI()

@mi_app.get("/")        
def msg_clientes(): #Función
    return{"Este es el proyecto de mis clientes."} #Valor retornado


lista_clientes = [
    {"id": 1, "nombre": "Lady", "email": "lady@gmail.com", "edad": 22, "descripcion": "NA"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "edad": 19, "descripcion": "NA"},
    {"id": 3, "nombre": "Ana", "email": "ana@gmail.com", "edad": 23, "descripcion": "NA"},
    {"id": 4, "nombre": "Carlos", "email": "carlos@gmail.com", "edad": 25, "descripcion": "NA"},
    {"id": 5, "nombre": "Sofía", "email": "sofia@gmail.com", "edad": 21, "descripcion": "NA"},
]

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
