#fitxer per les funcions que faran el CRUD de la taula estadistiques
from connection import *
from fastapi import HTTPException

#funcio per fer el READ de la taula estadistiques
def llegir_estadistiques(id):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #mirem si existeix l'id entrat
        cur.execute("SELECT * FROM estadistiques WHERE id_estadistica = %s", (id,))
        sql_result = cur.fetchone()
        #si l'id no existeix
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'ID= {id} no trobat.')
        #si l'id existeix, retornem el resultat
        return sql_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error a la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()

#definim el schema per estadistiques
def schema_estadistiques(lista) -> dict:
    return {
        "id_estadistica": lista[0],
        "id_usuari": lista[1],
        "partides_totals": lista[2],
        "partides_guanyades": lista[3],
        "millor_puntuacio": lista[4]
    }