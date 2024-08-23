from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum


class Cita(Base):
    __tablename__ = "tbb_citas"
    
    ID = Column(Integer, primary_key=True, index=True)
    Hora_Cita = Column(DateTime)
    Telefono = Column(String(20)) 
    Correo_Electronico = Column(String(255))
    Motivo_Cita = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    