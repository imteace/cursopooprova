from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Curso(BaseModel):
        
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    dia: int