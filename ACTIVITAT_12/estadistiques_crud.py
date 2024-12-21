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


#funcio per fer insert a la taula estadistiques
def insert_estadistiques(estadistica):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #preparem l'insert per la taula estadistiques
        cur.execute("INSERT INTO estadistiques (id_usuari, partides_totals, partides_guanyades, millor_puntuacio) VALUES (%s, %s, %s, %s)", (estadistica.id_usuari, estadistica.partides_totals, estadistica.partides_guanyades, estadistica.millor_puntuacio))
        #desem els canvis a la taula/bbdd
        conn.commit()
        return {"message": "Nova entrada a estadistiques realitzada amb exit"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error a la bbdd: {str(e)}')
    finally:
        cur.close()
        conn.close()


#funcio per esborrar una entrada de la taula estadistiques
def esborrar_estadistica(id):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #mirem si el id existeix
        cur.execute("SELECT * FROM estadistiques WHERE id_estadistica = %s", (id,))
        sql_result = cur.fetchone()
        #si no hi es
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'ID= {id} no trobat.')
        #si existeix
        cur.execute("DELETE FROM estadistiques WHERE id_estadistica = %s", (id,))
        conn.commit()
        return {"message": f'Entrada amb ID={id} esborrada correctament'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()



#funcio per editar una entrada de la taula estadistiques
def editar_estadistiques(id, edit_estadis):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #mirem si existeix l'id entrat
        cur.execute("SELECT * FROM estadistiques WHERE id_estadistica = %s", (id,))
        sql_result = cur.fetchone()
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'ID={id} no trobat.')
        #preparem el update ja que id existeix
        cur.execute("UPDATE estadistiques SET id_usuari = %s, partides_totals = %s, partides_guanyades = %s, millor_puntuacio = %s WHERE id_estadistica = %s", (edit_estadis.id_usuari, edit_estadis.partides_totals, edit_estadis.partides_guanyades, edit_estadis.millor_puntuacio, id))
        #desem els canvis
        conn.commit()
        return {"message": f'Entrada amb id={id} actualitzada amb exit.'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()





