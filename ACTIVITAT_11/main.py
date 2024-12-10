from fastapi import FastAPI, HTTPException
from read_cadena import *
from pydantic import BaseModel
from connection import *

app = FastAPI()

#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}


class Cadena(BaseModel):
    id_cadena: int
    cadena: str

#endpoint GET per retornar text començar partida
@app.get("/start_game/{id_cadena}")
async def comencar_partida(id_cadena):
    cadena = read_cadena_id(id_cadena)

    if cadena is None:
        raise HTTPException(status_code=404, detail="Cadena not found")

    #retorna json
    return {"id_cadena": cadena[0], "cadena": cadena[1]}


#endpoint per retornar l'abecedari
@app.get("/abecedari/{id}")
async def abecedari(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #fem la consulta sql per obtenir l'abecedari que volem des de l'id desitjat
        cur.execute("SELECT * FROM abecedaris WHERE id_abecedari = %s", (id,))
        sql_abecedari = cur.fetchone()

        #error de ID no trobat
        if sql_abecedari is None:
            raise HTTPException(status_code=404, detail="ID no trobat")

    #error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    #return format json
    return {"id_abecedari": sql_abecedari[0], "nom_abecedari": sql_abecedari[1], "abecedari": sql_abecedari[2]}
