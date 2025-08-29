from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"mensagem": "Olá, FastAPI!"}

class Login(BaseModel):
    id: int
    senha: str

db = {
    1: "1234", 
    2: "abcd"
}

@app.post("/login")
def auth(dados: Login):
    if dados.id in db and db[dados.id] == dados.senha:
        return {"status": "sucesso", "mensagem": "Login realizado!"}
    return {"status": "erro", "mensagem": "Usuário ou senha incorretos"}
