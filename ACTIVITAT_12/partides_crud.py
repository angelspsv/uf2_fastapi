#fitxer per les funcions que faran el CRUD de la taula partides
from connection import *
from fastapi import HTTPException



#funcio per fer el READ/llegir una entrada a la taula partides
def llegir_partides(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #mirem si l'id existeix
        cur.execute("SELECT * FROM partides WHERE id_partida = %s", (id,))
        sql_select = cur.fetchone()
        #si no existeix
        if sql_select is None:
            raise HTTPException(status_code=404, detail=f'El id={id} entrat no existeix.')
        #si existeix
        return sql_select
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problema amb la base de dades. {str(e)}')
    finally:
        cur.close()
        conn.close()



#definim el schema per la taula partides
def partida_schema(sql_select) -> dict:
    return {
        "id_partida": sql_select[0],
        "id_paraula": sql_select[1],
        "id_usuari": sql_select[2],
        "intents": sql_select[3],
        "punts_partida": sql_select[4],
        "resultat_partida": sql_select[5]
    }

