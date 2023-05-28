from sqlalchemy import Column, Integer, String, Date, Float
from ETLAPI.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer)
    transaction_date = Column(Date)
    amount = Column(Float)
    merchant_name = Column(String(100))
