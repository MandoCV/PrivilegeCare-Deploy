from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.tbc_organos, config.db
import schemas.tbc_organos
import models.tbc_organos
from typing import List

tbc_organos = APIRouter()

models.tbc_organos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@tbc_organos.get("/organos/", response_model=List[schemas.tbc_organos.Organo], tags=["Organos"])
def read_organos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_organos = crud.tbc_organos.get_organos(db=db, skip=skip, limit=limit)
    return db_organos

@tbc_organos.get("/organo/{id}", response_model=schemas.tbc_organos.Organo, tags=["Organos"])
def read_organo(id: int, db: Session = Depends(get_db)):
    db_organo = crud.tbc_organos.get_organo(db=db, id=id)
    if db_organo is None:
        raise HTTPException(status_code=404, detail="Organo no encontrado")
    return db_organo

@tbc_organos.post("/organo/", response_model=schemas.tbc_organos.Organo, tags=["Organos"])
def create_organo(organo: schemas.tbc_organos.OrganoCreate, db: Session = Depends(get_db)):
    db_organo = crud.tbc_organos.get_organo_by_nombre(db, nombre=organo.Nombre)
    if db_organo:
        raise HTTPException(status_code=400, detail="Organo existente intenta nuevamente")
    return crud.tbc_organos.create_organo(db=db, organo=organo)

@tbc_organos.put("/organo/{id}", response_model=schemas.tbc_organos.Organo, tags=["Organos"])
def update_organo(id: int, organo: schemas.tbc_organos.OrganoUpdate, db: Session = Depends(get_db)):
    db_organo = crud.tbc_organos.update_organo(db=db, id=id, organo=organo)
    if db_organo is None:
        raise HTTPException(status_code=404, detail="Organo no existe, no actualizado")
    return db_organo

@tbc_organos.delete("/organo/{id}", response_model=schemas.tbc_organos.Organo, tags=["Organos"])
def delete_organo(id: int, db: Session = Depends(get_db)):
    db_organo = crud.tbc_organos.delete_organo(db=db, id=id)
    if db_organo is None:
        raise HTTPException(status_code=404, detail="Organo no existe, no se pudo eliminar")
    return db_organo
