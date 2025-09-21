from fastapi import FastAPI
from auth import router as auth_router
from areaaluno import router as aluno_router
from areaprofessor import router as prof_router

app = FastAPI()

# Inclui os routers com prefixos
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(aluno_router, prefix="/aluno", tags=["Aluno"])
app.include_router(prof_router, prefix="/prof", tags=["Professor"])
