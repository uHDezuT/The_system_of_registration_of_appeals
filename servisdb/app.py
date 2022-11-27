from fastapi import FastAPI
from schema import *

import db_models
from db_connect import engine, SessionLocal

### DB
db_models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### END DB

app = FastAPI()
