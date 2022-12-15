from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class ProductTypeDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    active: Optional[datetime]
    inactive: Optional[datetime]