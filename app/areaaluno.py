from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

cursos = {
    "Python": "Introdução Python",
    "Java": "Introdução Java",
    "Front-end": "Fundamentos em Desenvolvimento Web"
}

@app.get("/cursos")
def catologo():
    return {"mensagem": "Cursos disponiveis", "cursos": cursos}

meus_cursos = {}

@app.get("/meus-cursos")
def acessar_cursos():
    return {"mensagem": "Meus cursos", "acessar": meus_cursos}

class Matricula(BaseModel):
    curso_matricula: str

@app.post("/matricula")
def matricular(dados: Matricula):
    curso = dados.curso_matricula

    if curso not in cursos:
        return {"status": "Erro", "mensagem": "Curso não encontrado no catálogo"}

    if curso in meus_cursos:
        return {"status": "Erro", "mensagem": "Você já está matriculado neste curso"}
    
    meus_cursos[curso] = cursos[curso]
    return {"status": "Sucesso", "mensagem": f"Matrícula realizada no curso {curso}"}