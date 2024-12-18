from typing import List
from fastapi import FastAPI, HTTPException
from connection import *
from paraules_crud import *
from pydantic import BaseModel


app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def prova():
    return {"message": "Hola!"}



#endpoint per llegir una entrada de la taula PARAULES
@app.get("/paraules/read/{id}", response_model=dict)
async def read_paraula(id: int):
    paraula = llegir_paraula(id)

    if paraula is None:
        raise HTTPException(status_code=404, detail=f'Paraula amb {id} no trobada')

    # returnem el resultat en format json
    return paraula_schema(paraula)


#endpoint per esborrar/eliminar un mot de la taula paraules
@app.delete("/paraules/delete/{id}")
async def delete_paraula(id: int):
    resultat = esborrar_mot(id)
    return resultat


class Paraula(BaseModel):
    paraula: str
    tematica: str
    id_abecedari: int

#endpoint per crear/inserir una nova paraula a la taula PARAULES
@app.post("/paraules/create/", response_model=dict)
def create_paraula(paraula: Paraula):
    result = insert_new_word(paraula)
    return result



@app.put("/paraules/update/{id}")
def update_paraules(id: int, updated_paraula: Paraula):
    resultat = modifica_paraula(id, updated_paraula)
    return resultat
