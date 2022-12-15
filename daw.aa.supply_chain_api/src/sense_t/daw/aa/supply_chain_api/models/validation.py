from sqlalchemy import Column, String, Text, Integer, DateTime, JSON
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

from .base import Base


class Validation(Base):
    __tablename__ = 'validations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_uid = Column(String(255),
                         ForeignKey('products.uid'),
                         nullable=True)
    product_type_id = Column(Integer,
                             ForeignKey('product_types.id'),
                             nullable=True)
    # client_id = Column(Integer, ForeignKey('clients.id'), nullable=True)

    request_time = Column(DateTime, default=func.now(), index=True)
    request_product_uid = Column(String(255), nullable=True)
    request_source = Column(String(255), nullable=True, index=True)
    request_headers = Column(JSON)
    request_url = Column(Text)
    request_method = Column(String(255))

    # product = relationship("Product", lazy="joined")
    # client = relationship("Client", lazy="joined")