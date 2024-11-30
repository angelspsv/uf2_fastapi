from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connection import *
import random

app = FastAPI()


class Option(BaseModel):
    option: str


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}


@app.get("/penjat/tematica/opcions", response_model=list[Option])
async def tematica_opcions():
    #codi per obtenir les tematiques

    conn = connection_db()
    cur = conn.cursor()
    try:
        sql_tematica = "SELECT theme FROM tematicas"
        cur.execute(sql_tematica)
        #desem la query answer
        tematiques = cur.fetchall()

        #fem servir un set per obtenir les tematiques no repetides
        mySet_temas = set(tematica[0] for tematica in tematiques)

        #fem una llista de Tematica nomes amb els temas no repetits
        result = [Option(option=theme) for theme in mySet_temas]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtenir les tematiques: {str(e)}")

        # tanquem els recursos/connexions
    finally:
        cur.close()
        conn.close()

    return result





@app.get("/penjat/tematica/{option}", response_model=list[Option])
async def tematica_random_word(option):
    #codi per obtenir un mot random a partir d'una tematica rebuda per parametre
    #obtenim les tematiques
    conn = connection_db()
    cur = conn.cursor()
    try:
        sql_tematiques_mots = "SELECT * FROM tematicas"
        cur.execute(sql_tematiques_mots)
        #desem la query answer
        tematiques_mots = cur.fetchall()

        #lista con el tema buscado
        listas_con_tema_buscado = [sublista for sublista in tematiques_mots if option in sublista]
        #en cuantos resultados aparece la palabra buscada
        cuantos = len(listas_con_tema_buscado)

        if cuantos == 0:
            raise HTTPException(status_code=404, detail="Tema no trobat")

        #num random de entre los existentes
        num_aleatorio = random.randint(1, cuantos)
        #coger lista segun nuemero random
        lista_random = listas_con_tema_buscado[num_aleatorio-1][1]

        resultat = [Option(option=lista_random)]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtenir els mots de la tematica: {str(e)}")

        # tanquem els recursos/connexions
    finally:
        cur.close()
        conn.close()
    return resultat















