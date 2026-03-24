from sqlalchemy.orm import Session
from models import Curso
import dtos

def get_cursos(db: Session):
    return db.query(Curso).all()

def find_curso(db: Session, curso_id: int):
    return db.query(Curso).filter(Curso.id == curso_id).first()

def crear_curso(db: Session, curso: dtos.CursoCreate):
    db_curso = Curso(
        nombre_del_curso=curso.nombre_del_curso,
        id_del_profesor=curso.id_del_profesor,
        descripcion=curso.descripcion,
        fecha_de_inicio=curso.fecha_de_inicio,
        fecha_de_fin=curso.fecha_de_fin
    )
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso
def actualizar_curso(db: Session, curso_id: int, curso_update: dtos.CursoCreate):
    db_curso = find_curso(db, curso_id)
    if db_curso is None:
        return None
    db_curso.nombre_del_curso = curso_update.nombre_del_curso
    db_curso.id_del_profesor = curso_update.id_del_profesor
    db_curso.descripcion = curso_update.descripcion
    db_curso.fecha_de_inicio = curso_update.fecha_de_inicio
    db_curso.fecha_de_fin = curso_update.fecha_de_fin
    db.commit()
    db.refresh(db_curso)
    return db_curso

def eliminar_curso(db: Session, curso_id: int):
    db_curso = find_curso(db, curso_id)
    if db_curso is None:
        return None
    db.delete(db_curso)
    db.commit()
    return db_curso