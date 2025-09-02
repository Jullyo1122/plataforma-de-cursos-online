from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

cursos = {
    "Python": "Introdução Python",
    "Java": "Introdução Java",
    "Front-end": "Fundamentos em Desenvolvimento Web"
}

@app.get("/")
def catologo():
    {"mensagem": "Cursos disponiveis", "cursos": cursos}
