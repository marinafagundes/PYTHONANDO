# tabela do banco de dados
# contém classes do banco de dados
# contas

from sqlmodel import Field, SQLModel, create_engine, Relationship
from enum import Enum
from datetime import date

class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'

class Status(Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'

class Tipos(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saida'

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)
    valor: float

class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key = "conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default = Tipos.ENTRADA)
    valor: float
    data: date

# criar o banco de dados
# sqlite é um banco de dados nativo do python
sqlite_file_name = "database.db"  # arquivo com todos os dados
# banco de dados que desejamos trabalhar
sqlite_url = f"sqlite:///{sqlite_file_name}" 

# conexão com o banco
# echo = True --> informar todos os erros de forma descritiva no terminal
engine = create_engine(sqlite_url, echo=True) 

# verifica se o arquivo está rodando por ele mesmo
# cria todas as tabelas
if __name__ == "__main__":  
    SQLModel.metadata.create_all(engine) 