from sqlalchemy import Column, String, Text, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

from .base import Base


class Product(Base):
    __tablename__ = 'products'

    uid = Column(String(255), primary_key=True)
    product_type_id = Column(Integer, ForeignKey('product_types.id'))

    registered_at = Column(DateTime, default=func.now())

    active = Column(DateTime, nullable=True)
    inactive = Column(DateTime, nullable=True)
    # registered_by = Column(String(255), nullable=False)

    # product_type = relationship("ProductType", lazy="joined")