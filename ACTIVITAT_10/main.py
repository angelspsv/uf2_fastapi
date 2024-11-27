from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connection import *

app = FastAPI()


class Tematica(BaseModel):
    word: str
    theme: str


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}


@app.get("/penjat/tematica/opcions", response_model=list[Tematica])
async def tematica_opcions():
    #codi per obtenir les tematiques
    return









