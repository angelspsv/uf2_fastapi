from fastapi import FastAPI, HTTPException
from read_cadena import *
from pydantic import BaseModel

app = FastAPI()

#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}


class Cadena(BaseModel):
    id_cadena: int
    cadena: str


@app.get("/start_game/{id_cadena}")
async def comencar_partida(id_cadena):
    cadena = read_cadena_id(id_cadena)

    if cadena is None:
        raise HTTPException(status_code=404, detail="Cadena not found")

    #retorna json
    return {"id_cadena": cadena[0], "cadena": cadena[1]}

