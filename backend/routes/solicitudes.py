from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models.solicitudes
import crud.solicitudes
import config.db
import schemas.solicitudes
from typing import List
from portadortoken import Portador

request = APIRouter()

models.solicitudes.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@request.get("/solicitudes/", response_model=List[schemas.solicitudes.Solicitud], tags=["Solicitudes"], dependencies=[Depends(Portador)])
def read_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_request = crud.solicitudes.get_requests(db=db, skip=skip, limit=limit)
    return db_request

@request.post("/solicitudes/{id}", response_model=schemas.solicitudes.Solicitud, tags=["Solicitudes"], dependencies=[Depends(Portador)])
def read_request(id: int, db: Session = Depends(get_db)):
    db_request = crud.solicitudes.get_request(db=db, id=id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Solicitud no existe")
    return db_request

@request.post("/solicitudes/", response_model=schemas.solicitudes.Solicitud, tags=["Solicitudes"], dependencies=[Depends(Portador)])
def create_request(request: schemas.solicitudes.SolicitudCreate, db: Session = Depends(get_db)):
    return crud.solicitudes.create_request(db=db, req=request)

@request.put("/solicitudes/{id}", response_model=schemas.solicitudes.Solicitud, tags=["Solicitudes"], dependencies=[Depends(Portador)])
def update_request(id: int, request: schemas.solicitudes.SolicitudUpdate, db: Session = Depends(get_db)):
    db_request = crud.solicitudes.update_request(db=db, id=id, req=request)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Solicitud no existe, no actualizada")
    return db_request

@request.delete("/solicitudes/{id}", response_model=schemas.solicitudes.Solicitud, tags=["Solicitudes"], dependencies=[Depends(Portador)])
def delete_request(id: int, db: Session = Depends(get_db)):
    db_request = crud.solicitudes.delete_request(db=db, id=id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Solicitud no existe, no se pudo eliminar")
    return db_request
