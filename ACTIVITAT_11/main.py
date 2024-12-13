from fastapi import FastAPI, HTTPException
from read_cadena import *
from pydantic import BaseModel
from connection import *
from abcd_query import *
from estadistiques_sql import *

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


# base model per intents
class Intents(BaseModel):
    intents: int

# endpoint per desar els intents amb un POST
@app.post("/intents/")
async def intents(ints):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #faig l'insert a la taula partida amb el nou intent
        cur.execute("INSERT INTO partides (id_paraula, id_usuari, intents, punts_partida, resultat_partida) VALUES (%s, %s, %s, %s, %s)", (2, 1, ints, 2, 4))
        conn.commit()

    except psycopg2.Error as e:
        # per errors especifics de la bbdd
        raise HTTPException(status_code=500, detail=f"Error amb la base de dades: {str(e)}")

    finally:
        # tanquem els recursos oberts
        cur.close()
        conn.close()

    #retornem el nombre de intents
    return {"intents": ints}



#endpoint per retornar l'abecedari
@app.get("/abecedari/{id}")
async def abecedari(id: int):
    abecedario = abc_query(id)

    if abecedario is None:
        raise HTTPException(status_code=404, detail="Abecedari not found")

    # fem una instancia de model i la retornem
    abecedari_json = Abecedari(
        id_abecedari=abecedario[0],
        nom_abecedari=abecedario[1],
        abecedari=abecedario[2],
    )

    #return format json
    return abecedari_json







# endpoint per renderitzar el text punts partides actuals, total partides, partides guanyades, partida amb mes punts des de la meva taula Estadistiques
@app.get("/estadistiques/{id_usuari}")
async def estadistiques(id_usuari: int):
    resultat_sql = estadistiques_query(id_usuari)

    if resultat_sql is None:
        raise HTTPException(status_code=404, detail="User not found")

    # return format json fet manualment
    return {"punts_partida": resultat_sql[0], "partides_totals": resultat_sql[1], "partides_guanyades": resultat_sql[2], "millor_puntuacio": resultat_sql[3]}


