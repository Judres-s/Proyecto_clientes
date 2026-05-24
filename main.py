from fastapi import FastAPI

mi_app= FastAPI()

@mi_app.get("/")
def msg_clientes():
    return{"Este es el proyecto de mis clientes."}


@mi_app.get("/Lista")
def de_clientes():
    return ["Y mis clientes son:", "Marco","Antonio","Ximena","Cecilia","Alejandra","Sofia"]