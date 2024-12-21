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

#funcio per esborrar una partida de la taula PARTIDES
def esborrar_partida(id):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #mirem si existeix l'id
        cur.execute("SELECT * FROM partides WHERE id_partida = %s", (id,))
        sql_result = cur.fetchone()
        #si id no esta
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'ID {id} no trobat.')
        #si l'id existeix faig la query per esborrar l'entrada amb id=X
        cur.execute("DELETE FROM partides WHERE id_partida = %s", (id,))
        # desem els canvis a la base de dades; de nou ens cal fer la connexio a la bbdd
        conn.commit()
        return {"message": f'Entrada amb id {id} esborrada correctament'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la base de dades. {str(e)}')
    finally:
        cur.close()
        conn.close()



#funcio per fer INSERT/CREATE a la taula PARTIDES
def insert_partides(partida):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #preparem l'insert
        cur.execute("INSERT INTO partides (id_paraula, id_usuari, intents, punts_partida, resultat_partida) VALUES (%s, %s, %s, %s, %s)", (partida.id_paraula, partida.id_usuari, partida.intents, partida.punts_partida, partida.resultat_partida))
        #desem l'insert a la base de dades
        conn.commit()
        return {"message": "Nova entrada a la taula Partides"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()


