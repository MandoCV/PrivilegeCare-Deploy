from typing import List,Union
from pydantic import BaseModel
from datetime import datetime



class CitasBase(BaseModel):
    ID: int
    Hora_Cita:datetime
    Telefono:str
    Correo_Electronico:str
    Motivo_Cita:str
    Estatus:bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    
    
class CitasCreate(CitasBase):
    pass
class CitasUpdate(CitasBase):
    pass
class Citas(CitasBase):
    ID: int

    class Config:
        orm_mode = True