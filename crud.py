from sqlalchemy.orm import Session

from db import Price

def get_prices(db: Session):
    return db.query(Price).all()
