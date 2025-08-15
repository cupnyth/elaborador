from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresas'
    
    id = Column(Integer, primary_key=True)
    razao = Column(String(100), nullable=False)
    cnpj = Column(String(18), nullable=False)
    contato = Column(Text)
    endereco = Column(Text)
    municipio = Column(Text)
    criado_em = Column(TIMESTAMP, default=func.now())