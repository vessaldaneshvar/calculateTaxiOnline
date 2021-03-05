from typing import Optional, List
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

import crud, schemas
from db import Price, Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/prices/', response_model=List[schemas.Price])
def prices(db: Session = Depends(get_db)):
    db_price = crud.get_prices(db)
    if db_price:
        return db_price