import os
from fastapi import FastAPI
import uvicorn
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from fastapi.middleware.cors import CORSMiddleware

#importacion de rutas del modulo de pediatria
from routes.Pediatria.nacimientos import baby
from routes.Pediatria.viewCiudad import view1
from routes.Pediatria.viewGenero import view2
from routes.Pediatria.vacunas import vacuna

app=FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un hospital"
)

#permite inserciones para el front desde cualquier origen
#lo utiliza el modulo de pediatria para hacer prueba de insecion


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite cualquier encabezado
)

app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
#rutas para el modulo de pediatria
app.include_router(baby, prefix="/pediatria")
app.include_router(view1, prefix="/pediatria")
app.include_router(view2, prefix="/pediatria")
app.include_router(vacuna, prefix="/pediatria")
# Para desplegar el proyecto en render 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

print ("Hola bienvenido a mi backend")
