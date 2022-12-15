from sqlalchemy import Column, String, Text, Integer, DateTime

from .base import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, default=None, nullable=True)
    product_url = Column(Text, default=None, nullable=True)
    icon = Column(Text, default=None, nullable=True)

    deleted = Column(DateTime, default=None)