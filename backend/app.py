from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
# Programacion Quirurgica
from routes.cirugia import cirugia_router
from routes.horarios import horarios
from routes.espacios import espacio

app=FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
# Programacion Quirurgica
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)

print ("Hola bienvenido a mi backend")
