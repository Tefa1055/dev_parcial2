from contextlib import asynccontextmanager
from enum import unique
from lib2to3.pytree import Base

from fastapi import FastAPI
from utils.connection_db import init_db
from sqlalchemy import column, integer, string, boolean, DateTime, ForeignKey, enum

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(integer, primary_key=True, index=True)
    nombre = Column(string(50), index=True)
    email = Column(string(100), unique=True, index=True)
    estado = Column(enum(EstadoUsuario), default=EstadoUsuario.ACTIVO)

class EstadoUsuario(str, enum.Enum):
    __tablename__ = "estado_usuario"
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    ELIMINADO = "ELIMINADO"

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
