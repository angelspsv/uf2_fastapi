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


# metode per fer el DELETE de la taula abecedaris
def delete_abecedari(id):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #mirem si existeix l'id
        cur.execute("SELECT * FROM abecedaris WHERE id_abecedari = %s", (id,))
        #resultat de la query
        resultat = cur.fetchone()

        if resultat is None:
            raise HTTPException(status_code=404, detail=f'ID {id} abecedari no trobat')

        #fem la query per esborrar l'abecedari desitjat
        cur.execute("DELETE FROM abecedaris WHERE id_abecedari = %s", (id,))

        #desem els canvis a la base de dades; de nou ens cal fer la connexio a la bbdd
        conn.commit()
        return {"message": f"S'ha esborrat correctament l'abecedari amb id {id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durant l'eliminació de l'entrada: {str(e)}")
    finally:
        cur.close()
        conn.close()


# funcio que fara un insert de nou abecedari a la taula abecedaris
def nou_abecedari(abecedari):
    try:
        conn = connection_db()
        cur = conn.cursor()
        #preparem l'insert de la nova entrada
        cur.execute("INSERT INTO abecedaris (nom_abecedari, abecedari) VALUES (%s, %s)", (abecedari.nom_abecedari, abecedari.abecedari))
        #desem els canvis a la bbdd
        conn.commit()

        return {"message":"nova entrada realitzada a la taula abecedari"}
    except psycopg2.Error as e:
        # per errors especifics de la bbdd
        raise HTTPException(status_code=500, detail=f"Error amb la base de dades: {str(e)}")
    finally:
        cur.close()
        conn.close()


# funcio per modificar (PUT/UPDATE) una entrada de la taula abecedaris
def editar_abecedari(id, edit_abecedari):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #mirem si l'id existeix
        cur.execute("SELECT * FROM abecedaris WHERE id_abecedari = %s", (id,))
        sql_result = cur.fetchone()

        #si no existeix l'id entrat, excepcio
        if sql_result is None:
            raise HTTPException(status_code=404, detail=f'Id {id} no tobat')

        #si existeix fem l'update de la entrada amb id X
        cur.execute("UPDATE abecedaris SET nom_abecedari = %s, abecedari = %s WHERE id_abecedari = %s", (edit_abecedari.nom_abecedari, edit_abecedari.abecedari, id))
        conn.commit()

        return {"message":"Entrada abecedari actualitzada amb exit"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error amb la base de dades: {str(e)}")
    finally:
        cur.close()
        conn.close()