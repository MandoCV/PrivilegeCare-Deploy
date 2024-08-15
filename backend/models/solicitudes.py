from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyEstatus(str, enum.Enum):
    Registrada = "Registrada"
    Programada = "Programada"
    Cancelada = "Cancelada"
    Reprogramada = "Reprogramada"
    En_Proceso = "En Proceso"
    Realizada = "Realizada"

class MyPrioridad(str, enum.Enum):
    Urgente = "Urgente"
    Alta = "Alta"
    Moderada = "Moderada"
    Emergente = "Emergente"
    Normal = "Normal"

class Solicitud(Base):
    __tablename__ = "tbd_solicitudes"

    ID = Column(Integer, primary_key=True, index=True)
    Paciente_ID = Column(Integer)
    Medico_ID = Column(Integer)
    Servicio_ID = Column(Integer)
    Prioridad = Column(Enum(MyPrioridad))
    Descripcion = Column(String(250))
    Estatus = Column(Enum(MyEstatus))
    Estatus_Aprobacion = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)