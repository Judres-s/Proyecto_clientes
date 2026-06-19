from fastapi import FastAPI, HTTPException #HTTPException es para capturar errors
from pydantic import BaseModel #Biblioteca para definir modelos de datos

mi_app= FastAPI()

@mi_app.get("/")        
def msg_clientes(): #Función
    return{"Este es el proyecto de mis clientes."} #Valor retornado


@mi_app.get("/Lista")
def de_clientes():
    return ["Y mis clientes son:", "Marco","Antonio","Ximena","Cecilia","Alejandra","Sofia"]

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

