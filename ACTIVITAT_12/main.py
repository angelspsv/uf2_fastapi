from typing import List
from fastapi import FastAPI, HTTPException
from connection import *
from paraules_crud import *
from pydantic import BaseModel
from abecedaris_crud import *
from cadenas_crud import *
from partides_crud import *


app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def prova():
    return {"message": "Hola!"}



#endpoint per llegir una entrada de la taula PARAULES
@app.get("/paraules/read/{id}", response_model=dict)
async def read_paraula(id: int):
    paraula = llegir_paraula(id)
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
async def create_paraula(paraula: Paraula):
    result = insert_new_word(paraula)
    return result


#endpoint per modificar una paraula de la taula PARAULES
@app.put("/paraules/update/{id}", response_model=dict)
async def update_paraules(id: int, updated_paraula: Paraula):
    resultat = modifica_paraula(id, updated_paraula)
    return resultat



# endpoints del CRUD per la taula ABECEDARIS
@app.get("/abecedaris/read/{id}", response_model=dict)
async def read_abecedari(id: int):
    abecedari = llegir_abecedari(id)
    # returnem el resultat en format json
    return abecedari_schema(abecedari)


#endpoint per esborrar un abecedari
@app.delete("/abecedaris/delete/{id}")
async def esborrar_alfabet(id: int):
    resultat = delete_abecedari(id)
    return resultat


class Abecedari(BaseModel):
    nom_abecedari: str
    abecedari: str


#endpoint per fer INSERT/CREATE a la taula abecedaris
@app.post("/abecedaris/create/", response_model=dict)
async def insert_abecedari(abecedari: Abecedari):
    result = nou_abecedari(abecedari)
    return result


#endpoint per editar/UPDATE una entrada de la taula abecedaris
@app.put("/abecedaris/update/{id}", response_model=dict)
async def update_abecedari(id: int, abecedari: Abecedari):
    resultat = editar_abecedari(id, abecedari)
    return resultat



# Endpoints per la taula cadenas
#endpoint per llegir/READ entrada de la taula cadenas
@app.get("/cadenas/read/{id}", response_model=dict)
async def read_cadenas(id: int):
    resultat = llegir_cadena(id)
    #el resultat de la sql_query se la paso a cadenas_schema que retorna un json
    return cadenas_schema(resultat)


#endpoint per esborrar una entrada de la taula cadenas
@app.delete("/cadenas/delete/{id}")
async def delete_cadenas(id: int):
    resultado = borrar_cadenas(id)
    return resultado



class Cadena(BaseModel):
    cadena: str


#endpoint per fer entrades/CREATE a la taula CADENAS
@app.post("/cadenas/create/", response_model=dict)
async def create_cadena(cadena: Cadena):
    answer = insert_cadenas(cadena)
    return answer



#endpoint per editar (UPDATE) una entrada de la taula cadenas
@app.put("/cadenas/update/{id}", response_model=dict)
async def update_cadena(id: int, cadena: Cadena):
    respuesta = editar_cadena(id, cadena)
    return respuesta


# Endpoints CRUD per la taula PARTIDES
#endpoint (GET)/READ de la taula partides
@app.get("/partides/read/{id}", response_model=dict)
async def read_partida(id: int):
    entrada = llegir_partides(id)
    return partida_schema(entrada)



#endpoint per esborrar una entrada de la taula partides
@app.delete("/partides/delete/{id}")
async def delete_partida(id: int):
    result = esborrar_partida(id)
    return result



class Partida(BaseModel):
    id_paraula: int
    id_usuari: int
    intents: int
    punts_partida: int
    resultat_partida: int


#endpoint POST/CREATE per la taula PARTIDES
@app.post("/partides/create/", response_model=dict)
async def create_partida(partida: Partida):
    resultat = insert_partides(partida)
    return resultat



#endpoint per editar (UPDATE) una entrada de la taula partides
@app.put("/partides/update/{id}", response_model=dict)
async def update_partida(id: int, partida: Partida):
    resultado = editar_partida(id, partida)
    return resultado



