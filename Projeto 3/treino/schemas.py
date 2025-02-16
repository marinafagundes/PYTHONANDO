from ninja import ModelSchema, Schema
from .models import Alunos
from typing import Optional

# ModelSchema --> cria a representação a partir de uma Model
# Schema --> cria do zero uma representação dos dados que vão ser recebidos ou retornados por nosso endpoint

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']

# Alternativa
# class UpdateAlunosSchema(Schema):
        # nome: str
        # email: str
        # faixa: str
        # data_nascimento: Optional[str]

class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_necessarias_para_proxima_faixa: int

class AulaRealizadaSchema(Schema):
    qtd: Optional[int] = 1
    email_aluno: str