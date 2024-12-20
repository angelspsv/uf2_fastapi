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


# funcio per fer INSERT/CREATE a la taula cadenas
def insert_cadenas(cadena):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #preparem insert_query
        cur.execute("INSERT INTO cadenas (cadena) VALUES (%s)", (cadena.cadena,))
        #desem els canvis a la taula
        conn.commit()
        return {"message":"nou insert realitzat correctament"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la base de dades: {str(e)}')

    finally:
        cur.close()
        conn.close()



# funcio per editar (UPDATE) una entrada de la taula cadenas
def editar_cadena(id, edited_cadena):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #mirem si l'id existeix a la taula cadenas
        cur.execute("SELECT * FROM cadenas WHERE id_cadena = %s", (id,))
        sql_result = cur.fetchone()
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat')
        #si l'id existeix fem l'update de la entrada existent
        cur.execute("UPDATE cadenas SET cadena = %s WHERE id_cadena = %s", (edited_cadena.cadena, id))
        conn.commit()
        return {"message":f'Entrada amb id {id} actualitzada amb exit'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la base de dades {str(e)}')
    finally:
        cur.close()
        conn.close()

