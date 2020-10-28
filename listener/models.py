import db

from sqlalchemy import Column, Integer, String, Float


class Mensaje(db.Base):
    __tablename__ = 'mensaje'

    id = Column(Integer, primary_key=True)
    mensaje = Column(String, nullable=False)

    def __init__(self, mensaje):
        self.mensaje = mensaje

