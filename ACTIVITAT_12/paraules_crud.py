from connection import *
from pydantic import BaseModel
from fastapi import HTTPException

# fitxer pels metodes del CRUD que afecten la taula PARAULES

# metode per fer el read a la taula PARAULES
def llegir_paraula(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        # fem la consulta sql per obtenir l'abecedari que volem des de l'id desitjat
        cur.execute("SELECT * FROM paraules WHERE id_paraula = %s", (id,))
        sql_mot = cur.fetchone()

        # error de ID no trobat
        if sql_mot is None:
            raise HTTPException(status_code=404, detail="ID no trobat")

    # error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    # returnem el resultat
    return sql_mot



