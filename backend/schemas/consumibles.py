from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import enum

class EstatusEnum(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    En_Revisión = "En Revisión"

class ConsumibleBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Cantidad: int
    Tipo: str
    Departamento_ID: int
    Estatus: EstatusEnum = EstatusEnum.Activo
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None
    Observaciones: Optional[str] = None
    Espacio_Medico: str

class ConsumibleCreate(ConsumibleBase):
    pass

class ConsumibleUpdate(BaseModel):
    pass

class Consumible(ConsumibleBase):
    ID: int

    class Config:
        orm_mode = True

