import inspect
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from sqlalchemy import Select
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DECIMAL

# Criando a declarative base, que será herdada pelas classes

Base = declarative_base()

# Criando as classes

class Cliente(Base):
    
    __tablename__ = "info_cliente"
    
    # Atributos
    
    id = Column(Integer, primary_key=True, autoincrement=True) 
    nome = Column(String)
    cpf = Column(Integer, nullable=False)
    endereco = Column(Integer)
    
    # Definindo o relacionamento
    
    conta = relationship(
        "Conta", back_populates="cliente"
    )

class Conta(Base):
    
    __tablename__ = "info_conta"
    
    # Atributos
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("info_cliente.id"), nullable= False)
    saldo = Column(DECIMAL)
    
    # Definindo o relacionamento
    
    cliente = relationship(
       "Cliente", back_populates="conta"
    )
    
# Definindo a engine

engine = create_engine("sqlite://")

# Criando o metadata do banco de dados na aplicação

Base.metadata.create_all(engine)

# Persistindo as informações

with Session(engine) as session:
    
    # Criando as instâncias de classes que serão permitidas no bd
    
    cliente_0 = Cliente(
        nome = 'luiz farias',
        cpf = 56460951829,
        endereco = 'avenida santa fé n 575, francisco morato, são paulo',
        conta = [Conta(
            tipo = "corrente",
            agencia = '0001',
            num = 12,
            saldo = 0                   
        )]
    )
    
    # Adicionando as informações
    
    session.add_all([cliente_0])
    
    # Comitando as informações
    
    session.commit()

# Recuoerando informacões

# Criando o statement que irá ser execudado no bd, come se fosse uma query

stmt = Select(Cliente, Conta).join_from(Conta, Cliente)

# Gerando a conexão com o bd

connection = engine.connect()

# Guardando os resuiltados em uma variável indexada

results = connection.execute(stmt).fetchall()

# Exibindo o statement/query criado

print(stmt)

# Exibindo os resultados do statement

for chave in results:
     print(chave)