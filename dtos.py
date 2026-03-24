from pydantic import BaseModel
import datetime

class CursoCreate(BaseModel):
    nombre_del_curso: str
    id_del_profesor: int
    descripcion: str
    fecha_de_inicio: datetime.date
    fecha_de_fin: datetime.date

class CursoResponse(BaseModel):
    id: int
    nombre_del_curso: str
    id_del_profesor: int
    descripcion: str
    fecha_de_inicio: datetime.date
    fecha_de_fin: datetime.date