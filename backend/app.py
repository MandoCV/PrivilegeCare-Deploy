from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.personal_medico import personal_medico
from routes.puestos_departamentos import puesto_departamento
from routes.puestos import puesto
from routes.departamentos import departamentos
from routes.areas_medicas import area_medica

app=FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(departamentos)
app.include_router(personal_medico)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(area_medica)


print ("Hola bienvenido a mi backend")
