from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"mensagem": "Olá, FastAPI!"}

class Login(BaseModel):
    id: int
    senha: str
    role: str

# Banco de dados simulado
db = {
    1: {"email": "teste@email.com", "senha": "1234", "role": "aluno"},
    2: {"email": "abc@email.com", "senha": "abcd", "role": "professor"}
}

@app.post("/login")
def auth(dados: Login):
    if dados.id in db and db[dados.id]["senha"] == dados.senha:
        return {"status": "sucesso", "mensagem": "Login realizado!", "role": db[dados.id]["role"]}
    return {"status": "erro", "mensagem": "Usuário ou senha incorretos"}


class Cadastro(BaseModel):
    email: str
    senha: str
    id: int
    role: str

@app.post("/cadastro")
def cad(dados: Cadastro):
    # Verifica se o id já existe
    if dados.id in db:
        return {"status": "erro", "mensagem": "ID já cadastrado"}
    # Verifica se o email já existe
    if any(u["email"] == dados.email for u in db.values()):
        return {"status": "erro", "mensagem": "Email já cadastrado"}
    # Adiciona novo usuário
    db[dados.id] = {"email": dados.email, "senha": dados.senha, "role": dados.role}
    return {"status": "sucesso", "mensagem": "Cadastro realizado!"}