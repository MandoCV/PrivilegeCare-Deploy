from typing import List, Union,Literal, Optional
from pydantic import BaseModel
from datetime import datetime, date
import models.persons
class PersonBase(BaseModel):
    Titulo_Cortesia: Optional[str]
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Fecha_Nacimiento: date
    Fotografia: Optional[str]
    Genero: str#List[Literal["Masculino", "Femenino", "Otro"]]
    Tipo_Sangre:str
    Estatus: Optional[bool]
    Fecha_Registro: Optional[datetime]
    Fecha_Actualizacion: Optional[datetime]

class PersonCreate(PersonBase):
    Titulo_Cortesia: Optional[str] = None
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Fecha_Nacimiento: date
    Fotografia: Optional[str] = None
    Genero: str#List[Literal["Masculino", "Femenino", "Otro"]]
    Tipo_Sangre: str
    Estatus: Optional[bool] = None
    Fecha_Registro: Optional[datetime]  = None
    Fecha_Actualizacion: Optional[datetime] = None
    

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    ID: int
    class Config:
        orm_mode = True


