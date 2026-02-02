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

class Pending(Base):
    # O nome da tabela no banco do Portal é 'pending'
    __tablename__ = 'pending'
    
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer) # Não precisamos da Relation completa aqui, só o ID resolve
    tipo_exame = Column(String)
    status = Column(String) # Vamos escrever "Concluido" aqui
    link_pdf = Column(String)