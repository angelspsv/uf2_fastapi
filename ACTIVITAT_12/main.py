from fastapi import FastAPI, HTTPException
from connection import *
from paraules_crud import *


app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def prova():
    return {"message": "Hola!"}



#endpoint per llegir una entrada de la taula PARAULES
@app.get("/paraules/read/{id}")
async def read_paraula(id: int):
    paraula = llegir_paraula(id)

    if paraula is None:
        raise HTTPException(status_code=404, detail=f'Paraula amb {id} no trobada')

    # returnem el resultat en format json
    return {"id_paraula": paraula[0], "paraula": paraula[1], "tematica": paraula[2], "id_abecedari": paraula[3]}


