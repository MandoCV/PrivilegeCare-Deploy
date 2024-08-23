from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
# Tambein agrega la importacion porfa
from routes.servicios_medicos import serviceM

app=FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print ("Hola bienvenido a mi backend")

# Armando podrias colocar esto en el app.py, le quitas el formato de comentario
# app.include_router(serviceM)