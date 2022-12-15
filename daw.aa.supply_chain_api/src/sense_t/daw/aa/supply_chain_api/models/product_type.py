from sqlalchemy import Column, String, Text, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class ProductType(Base):
    __tablename__ = 'product_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    name = Column(String(255), nullable=False)
    description = Column(Text, default=None, nullable=True)

    active = Column(DateTime, nullable=True)
    inactive = Column(DateTime, nullable=True)
    # client = relationship("Client", lazy="joined")
