from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: Optional[bool]
    Fecha_Registro: Optional[datetime]
    Fecha_Actualizacion: Optional[datetime]

class UserCreate(UserBase):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: Optional[bool] = None
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str] = None
    Correo_Electronico: Optional[str]= None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str]=None


