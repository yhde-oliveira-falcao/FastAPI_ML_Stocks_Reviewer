from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class StockDaily(Base):
    __tablename__ = 'stocks_daily'

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), index=True)
    date = Column(Date, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)


