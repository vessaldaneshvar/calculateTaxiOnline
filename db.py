from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, MetaData, Integer, Computed, ForeignKey, DateTime, String, func

Base = declarative_base()

class Price(Base):
    __tablename__ = "price"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    price = Column(Integer)
    sourceLat = Column(String(200))
    sourceLong = Column(String(200))
    destinationLat = Column(String(200))
    destinationLong = Column(String(200))


if __name__ == "__main__":
    engine = create_engine("sqlite:///data/db.sqlite")
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)