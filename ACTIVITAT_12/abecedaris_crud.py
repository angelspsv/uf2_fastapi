# fitxer amb els metodes del CRUD per la taula ABECEDARIS

from connection import *
from pydantic import BaseModel
from fastapi import HTTPException

#metode per fer el READ a la taula ABECEDARIS
def llegir_abecedari(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        # fem la consulta sql per veure si l'id existeix
        cur.execute("SELECT * FROM abecedaris WHERE id_abecedari = %s", (id,))
        sql_read = cur.fetchone()

        # error de ID no trobat
        if sql_read is None:
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat')

        # returnem el resultat
        return sql_read

    # error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()


#faig el schema d'abecedaris
def abecedari_schema(mot) -> dict:
    return {"id_abecedari": mot[0],
            "nom_abecedari": mot[1],
            "abecedari": mot[2]}


