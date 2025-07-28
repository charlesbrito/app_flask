from sqlalchemy import Integer, ForeignKey, Column, String
from database.conexao import Base

class Usuario(Base):

    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(Integer, nullable=False)
    email = Column(String, nullable=False )
    senha = Column(String, nullable=False)