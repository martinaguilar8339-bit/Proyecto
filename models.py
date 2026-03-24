from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Date
class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_del_curso = Column(String(255), index=True)
    id_del_profesor = Column(Integer, index=True)
    descripcion = Column(String(255), index=True)
    fecha_de_inicio = Column(Date)
    fecha_de_fin = Column(Date)