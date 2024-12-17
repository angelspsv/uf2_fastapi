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
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat')

    # error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    # returnem el resultat
    return sql_mot



#faig el schema de paraula
def paraula_schema(mot) -> dict:
    return {"id_paraula": mot[0],
            "paraula": mot[1],
            "tematica": mot[2],
            "id_abecedari": mot[3]}



#faig la funcio per esborrar una paraula de la taula PARAULES
def esborrar_mot(id):
    # a la funcio llegir_paraula(id) mirem si l'id del mot existeix a la taula paraules
    existeix = llegir_paraula(id)

    try:
        conn = connection_db()
        cur = conn.cursor()

        # esborrem l'alumne de la bbdd pel seu id_alumne
        cur.execute("DELETE FROM paraules WHERE id_paraula = %s", (id,))

        # desem els canvis
        conn.commit()

        # sms d'operació finalitzada amb èxit
        return {"message": "S'ha esborrat correctament"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durant l'eliminació de la paraula: {str(e)}")

    finally:
        cur.close()
        conn.close()


