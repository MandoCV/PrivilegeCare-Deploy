from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#configuracion de la base de datosm en aiven 
SQLALCHEMY_DATABASE_URL = "mysql://avnadmin:AVNS_YPv9gKHJKOhamUwUu3N@mysql-e331420-utxicotepec-f492.e.aivencloud.com:20907/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
