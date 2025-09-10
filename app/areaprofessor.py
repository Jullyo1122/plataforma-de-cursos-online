from fastapi import FastAPI
from pydantic import BaseModel
from areaaluno import cursos

app = FastAPI()
@app.get("/cursos")
def listar_cursos():
    return {"mensagem": "Catálogo de cursos", "cursos": cursos}

class NovoCurso(BaseModel):
    titulo_curso: str
    descricao: str

@app.post("/novocurso")
def criar_curso(dados: NovoCurso):
    if dados.titulo_curso in cursos:
         return {"status": "Erro", "mensagem": "Esse curso já está no catálogo"}
    
    cursos[dados.titulo_curso] = dados.descricao
    return {"status": "Sucesso", "mensagem": "Curso criado com sucesso", "curso": dados.titulo_curso}