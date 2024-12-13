from connection import *
from pydantic import BaseModel

class Cadena(BaseModel):
    id_cadena: int
    cadena: str

def read_cadena_id(id_cadena):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #fem la consulta sql per veure si existeix el id_cadena
        cur.execute("SELECT * FROM cadenas WHERE id_cadena = %s", (id_cadena,))
        cadena = cur.fetchone()

    #en cas d'error: no existeix l'id_cadena
    except Exception as e:
        print(f"Error al verificar el id_cadena: {e}")
        return None

    #si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    # retorna True o False de la consulta sql
    return cadena