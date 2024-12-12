from fastapi import HTTPException
from connection import *
from pydantic import BaseModel


# Model per estructurar el JSON
class Abecedari(BaseModel):
    id_abecedari: int
    nom_abecedari: str
    abecedari: str


#fitxer que fa el proces de la consulta sql a la taula abecedari
def abc_query(id_abc):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #fem la consulta sql per obtenir l'abecedari que volem des de l'id desitjat
        cur.execute("SELECT * FROM abecedaris WHERE id_abecedari = %s", (id_abc,))
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

    #returnem el resultat
    return sql_abecedari