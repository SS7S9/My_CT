from typing import Optional

from pydantic import BaseModel


class ClientDTO(BaseModel):
    id: int
    name: str
    description: Optional[str]
    product_url: str
    icon: Optional[str]
    deleted: Optional[str]


class ClientCreateDTO(BaseModel):
    name: str
    description: Optional[str]
    product_url: str
    icon: Optional[str]


class ClientUpdateDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    product_url: Optional[str]
    icon: Optional[str]
    deleted: Optional[str]