from fastapi import FastAPI
from pydantic import BaseModel
from auth import db

app = FastAPI()

cursos = {
    1: {"nome": "Python", "descricao": "Introdução Python", "alunos": []},
    2: {"nome": "Java", "descricao": "Introdução Java", "alunos": []},
    3: {"nome": "Front-end", "descricao": "Fundamentos em Desenvolvimento Web", "alunos": []}
}

@app.get("/cursos")
def catologo():
    return {"mensagem": "Cursos disponiveis", "cursos": cursos}

meus_cursos = {}

@app.get("/meus-cursos/{aluno_id}")
def acessar_cursos(aluno_id: int):
    return {"mensagem": "Meus cursos", "acessar": meus_cursos.get(aluno_id, [])}

class Matricula(BaseModel):
    aluno_id: int
    curso_id: int

@app.post("/matricula")
def matricular(dados: Matricula):
     aluno_id = dados.aluno_id  
     curso_id = dados.curso_id  
     if aluno_id not in db or db[aluno_id]["role"] != "aluno":
        return {"status": "erro", "mensagem": "Aluno não encontrado"}
     if curso_id not in cursos:
        return {"status": "Erro", "mensagem": "Curso não encontrado no catálogo"}
     if aluno_id not in meus_cursos:
        meus_cursos[aluno_id] = []
        if curso_id in meus_cursos[aluno_id]:
            return {"status": "Erro", "mensagem": "Você já está matriculado neste curso"}
     # adiciona no curso
     cursos[curso_id]["alunos"].append(aluno_id)
    # adiciona em "meus_cursos"
     meus_cursos[aluno_id].append(curso_id)
     return {"status": "Sucesso", "mensagem": f"Matrícula realizada no curso {cursos[curso_id]['nome']}"}