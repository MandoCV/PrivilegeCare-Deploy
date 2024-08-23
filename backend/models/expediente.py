from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base



class Expediente(Base):
    __tablename__ = "tbb_expediente"
    
    ID = Column(Integer, primary_key=True, index=True)
    Fecha_Consulta = Column(DateTime)
    Hora_Consulta = Column(DateTime)
    Diagnostico = Column(String(255))
    Tratamiento_Relacionado = Column(String(255))
    Observaciones = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

