from fastapi import HTTPException
from connection import *
from pydantic import BaseModel

# base model per intents
class Intents(BaseModel):
    intents: int


def intents_post(ints):
    try:
        conn = connection_db()
        cur = conn.cursor()
        # faig l'insert a la taula partida amb el nou intent
        cur.execute("INSERT INTO partides (id_paraula, id_usuari, intents, punts_partida, resultat_partida) VALUES (%s, %s, %s, %s, %s)", (1, 2, ints, 4, 8))
        conn.commit()

    except psycopg2.Error as e:
        # per errors especifics de la bbdd
        raise HTTPException(status_code=500, detail=f"Error amb la base de dades: {str(e)}")

    finally:
        # tanquem els recursos oberts
        cur.close()
        conn.close()

    # retornem el nombre de intents
    return {"intents": ints}