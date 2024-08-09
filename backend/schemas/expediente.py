from typing import List,Union
from pydantic import BaseModel
from datetime import datetime


class ExpedienteBase(BaseModel):
    
    ID:int
    Fecha_Consulta:datetime
    Hora_Consulta: datetime
    Diagnostico: str
    Tratamiento_Relacionado: str
    Observaciones: str
    Estatus:bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime


    
    
class ExpedienteCreate(ExpedienteBase):
    pass
class ExpedienteUpdate(ExpedienteBase):
    pass
class Expediente(ExpedienteBase):
    ID: int

    class Config:
        orm_mode = True