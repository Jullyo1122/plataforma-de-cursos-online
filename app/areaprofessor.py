from fastapi import FastAPI
from pydantic import BaseModel
from areaaluno import cursos
from auth import db

app = FastAPI()
@app.get("/cursos")
def listar_cursos():
    return {"mensagem": "Catálogo de cursos", "cursos": cursos}

class NovoCurso(BaseModel):
    id: int
    nome: str
    descricao: str

@app.post("/novocurso")
def criar_curso(dados: NovoCurso):
    # Verifica se o ID já existe
    if dados.id in cursos:
        return {"status": "Erro", "mensagem": "Esse ID de curso já existe"}
    # Verifica se já existe curso com esse nome
    for curso in cursos.values():
        if curso["nome"].lower() == dados.nome.lower():
            return {"status": "Erro", "mensagem": "Esse curso já está no catálogo"}
    cursos[dados.id] = {
        "nome": dados.nome,
        "descricao": dados.descricao,
        "alunos": []
    }
    return {"status": "Sucesso", "mensagem": "Curso criado com sucesso", "curso": dados.nome}

