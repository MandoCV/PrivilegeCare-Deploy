from typing import List, Union
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AparatoSistemaEnum(str, Enum):
    Circulatorio = 'Circulatorio'
    Digestivo = 'Digestivo'
    Respiratorio = 'Respiratorio'
    Nervioso = 'Nervioso'
    Muscular = 'Muscular'
    Esqueletico = 'Esquelético'
    Endocrino = 'Endocrino'
    Linfatico = 'Linfático'
    Inmunologico = 'Inmunológico'
    Reproductor = 'Reproductor'
    Urinario = 'Urinario'
    Sensorial = 'Sensorial'

class DisponibilidadEnum(str, Enum):
    Disponible = 'Disponible'
    NoDisponible = 'No Disponible'
    Reservado = 'Reservado'

class TipoEnum(str, Enum):
    Vital = 'Vital'
    NoVital = 'No Vital'

class OrganoBase(BaseModel):
    Nombre: str
    Aparato_Sistema: AparatoSistemaEnum
    Descripcion: str
    Disponibilidad: DisponibilidadEnum
    Tipo: TipoEnum
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class OrganoCreate(OrganoBase):
    pass

class OrganoUpdate(OrganoBase):
    pass

class Organo(OrganoBase):
    ID: int
    class Config:
        from_attributes = True
