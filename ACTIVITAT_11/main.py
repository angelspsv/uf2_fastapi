from fastapi import FastAPI, HTTPException
from read_cadena import *
from pydantic import BaseModel
from connection import *
from abcd_query import *

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

    #{"id_abecedari": abecedario[0], "nom_abecedari": abecedario[1], "abecedari": abecedario[2]}





# endpoint per renderitzar el text punts partides actuals, total partides, partides guanyades, partida amb mes punts des de la meva taula Estadistiques
@app.get("/estadistiques/{id_usuari}")
async def estadistiques(id_usuari):
    try:
        conn = connection_db()
        cur = conn.cursor()

        # fem la consulta sql per obtenir les dades de la taula estadistiques que volem amb l'id_usuari
        cur.execute("SELECT * FROM estadistiques WHERE id_usuari = %s", (id_usuari,))
        sql_estadistiques = cur.fetchone()

        # error de ID no trobat
        if sql_estadistiques is None:
            raise HTTPException(status_code=404, detail="ID_usuari no trobat")

    # error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    # return format json fet manualment
    return {"partides_totals": sql_estadistiques[2], "partides_guanyades": sql_estadistiques[3], "millor_puntuacio": sql_estadistiques[4]}



