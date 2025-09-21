from fastapi import APIRouter
from pydantic import BaseModel
from areaaluno import cursos

router = APIRouter()
@router.get("/cursos")
def listar_cursos():
    return {"mensagem": "Catálogo de cursos", "cursos": cursos}

class NovoCurso(BaseModel):
    id: int
    nome: str
    descricao: str

@router.post("/novocurso")
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

@router.put("/cursos/{id}")
def editar_curso(id: int, dados: NovoCurso):
    if id not in cursos:
        return {"status": "Erro", "mensagem": "Curso não encontrado"}
    cursos[id] = {
        "nome": dados.nome,
        "descricao": dados.descricao,
        "alunos": cursos[id]["alunos"]
    }
    return{"status": "Sucesso", "mensagem": "Curso atualizado", "curso": cursos[id]}

@router.delete("/cursos/{id}")
def excluir_curso(id: int):
     if id not in cursos:
        return {"status": "Erro", "mensagem": "Curso não encontrado"}
     curso_removido = cursos.pop(id)
     return {
        "status": "Sucesso",
        "mensagem": f"Curso '{curso_removido['nome']}' removido com sucesso"
    }
