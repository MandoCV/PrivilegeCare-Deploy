import models.Pediatria.vacunas
import schemas.Pediatria.vacunas
from sqlalchemy.orm import Session
import models, schemas


def get_vacunas_by_name_and_nacimientos_id(db: Session, nombre: str, nacimientos_id: int):
    return db.query(models.Pediatria.vacunas.Vacunas).filter(
        models.Pediatria.vacunas.Vacunas.vacuna_administrada == nombre, 
        models.Pediatria.vacunas.Vacunas.nacimientos_id == nacimientos_id
    ).first()


def get_vacunas_by_nacimientos_id(db: Session, nacimientos_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Pediatria.vacunas.Vacunas).filter(models.Pediatria.vacunas.Vacunas.nacimientos_id == nacimientos_id).offset(skip).limit(limit).all()


def get_vacunas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pediatria.vacunas.Vacunas).offset(skip).limit(limit).all()

def create_vacuna(db: Session, vacuna: schemas.Pediatria.vacunas.VacunaCreate):
    db_vacuna = models.Pediatria.vacunas.Vacunas(**vacuna.dict())
    db.add(db_vacuna)
    db.commit()
    db.refresh(db_vacuna)
    return db_vacuna
