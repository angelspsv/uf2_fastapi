from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from insertDATA.connection import *
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




#codi per obtenir un mot random a partir d'una tematica rebuda per parametre
@app.get("/penjat/tematica/{option}", response_model=list[Option])
async def tematica_random_word(option):

    conn = connection_db()
    cur = conn.cursor()
    try:
        # obtenim les tematiques després d'una consulta a la bbdd
        sql_tematiques_mots = "SELECT * FROM tematicas"
        cur.execute(sql_tematiques_mots)
        #desem la query answer
        tematiques_mots = cur.fetchall()

        #llista amb el tema cercat
        llistes_mot_tema_cercat = [sublista for sublista in tematiques_mots if option in sublista]
        #en quants resultats apareix el mot cercat
        quants = len(llistes_mot_tema_cercat)

        if quants == 0:
            raise HTTPException(status_code=404, detail="Tema no trobat")

        #num random de entre los existentes
        num_aleatori = random.randint(1, quants)
        #agafar mot de la llista triada segons el nombre random
        llista_random = llistes_mot_tema_cercat[num_aleatori-1][1]

        resultat = [Option(option=llista_random)]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtenir els mots de la tematica: {str(e)}")

        # tanquem els recursos/connexions
    finally:
        cur.close()
        conn.close()

    return resultat
