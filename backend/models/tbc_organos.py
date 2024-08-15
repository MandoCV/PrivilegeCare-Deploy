from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Text
from config.db import Base

class Organo(Base):
    __tablename__ = "tbc_organos"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(45), nullable=False)
    Aparato_Sistema = Column(Enum('Circulatorio', 'Digestivo', 'Respiratorio', 'Nervioso', 'Muscular', 'Esquelético', 'Endocrino', 'Linfático', 'Inmunológico', 'Reproductor', 'Urinario', 'Sensorial'), nullable=False)
    Descripcion = Column(Text, nullable=False)
    Disponibilidad = Column(Enum('Disponible', 'No Disponible', 'Reservado'), nullable=False)
    Tipo = Column(Enum('Vital', 'No Vital'), nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=True)
    Fecha_Registro = Column(DateTime, nullable=True)
    Estatus = Column(Boolean, default=True)
