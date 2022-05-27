from typing import Optional
from pydantic import BaseModel

class Email(BaseModel):
    email: str
    subject: str
    idtemplate: str