from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.cirugia import cirugia_router
from routes.horarios import horarios
from routes.espacios import espacio
from routes.areas_medicas import area_medica
from routes.bitacora import bitacora
from routes.consumibles import consumible
from routes.departamentos import departamentos
from routes.dispensaciones import dispensacion
from routes.estudios import estudios
#from routes.resultados_estudios import resultados_estudios
from routes.resultadosEstudios import resultadosEstudios
from routes.lotes import lote
from routes.medicamentos import medicamento
from routes.personal_medico import personal_medico
from routes.puestos import puesto
from routes.puestos_departamentos import puesto_departamento
from routes.solicitudes import request
from routes.tbb_aprobaciones import tbb_aprobaciones
from routes.tbc_organos import tbc_organos
from routes.Pediatria.nacimientos import baby
from routes.Pediatria.viewCiudad import view1
from routes.Pediatria.viewGenero import view2

app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de información de un hospital"
)

app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)
app.include_router(area_medica)
app.include_router(bitacora)
app.include_router(consumible)
app.include_router(departamentos)
app.include_router(dispensacion)
app.include_router(estudios)
app.include_router(resultadosEstudios)
#app.include_router(resultados_estudios)
app.include_router(lote)
app.include_router(medicamento)
app.include_router(personal_medico)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(request)
app.include_router(tbb_aprobaciones)
app.include_router(tbc_organos)
app.include_router(baby)
app.include_router(view1)
app.include_router(view2)

print("Hola, bienvenido a mi backend hospital")
