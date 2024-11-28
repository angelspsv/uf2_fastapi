from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connection import *

app = FastAPI()


class Tematica(BaseModel):
    #word: str
    theme: str


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}


@app.get("/penjat/tematica/opcions", response_model=list[Tematica])
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
        result = [Tematica(theme=theme) for theme in mySet_temas]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtenir les tematiques: {str(e)}")

        # tanquem els recursos/connexions
    finally:
        cur.close()
        conn.close()

    return result










