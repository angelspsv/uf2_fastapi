# fitxer amb els metodes del CRUD per la taula CADENAS

from connection import *
from pydantic import BaseModel
from fastapi import HTTPException

#funcio per fer el READ des de la taula cadenas
def llegir_cadena(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #preparem la query SELECT
        cur.execute("SELECT * FROM cadenas WHERE id_cadena = %s", (id,))
        sql_select = cur.fetchone()

        if sql_select is None:
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat')

        return sql_select
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error en la base de dades: {str(e)}')
    finally:
        cur.close()
        conn.close()


#schema de la taula cadenas
def cadenas_schema(sql_result) -> dict:
    return {
        "id_cadena": sql_result[0],
        "cadena": sql_result[1]
    }


#funcio per esborrar una entrada de la taula cadenas
def borrar_cadenas(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM cadenas WHERE id_cadena = %s", (id,))
        sql_select = cur.fetchone()

        if sql_select is None:
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat')

        #executem query per esborrar entrada segons l'id
        cur.execute("DELETE FROM cadenas WHERE id_cadena = %s", (id,))
        #desem els canvis a la taula cadenas
        conn.commit()

        return {"message":f'Entrada amb id {id} correctament esborrada.'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd: {str(e)}')
    finally:
        cur.close()
        conn.close()