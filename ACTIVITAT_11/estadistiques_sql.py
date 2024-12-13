from fastapi import HTTPException
from connection import *
from pydantic import BaseModel

def estadistiques_query(id_usuari):
    try:
        conn = connection_db()
        cur = conn.cursor()

        # fem la consulta sql per obtenir les dades de les taules estadistiques i partides que volem amb l'id_usuari
        cur.execute("SELECT p.punts_partida, e.partides_totals, e.partides_guanyades, e.millor_puntuacio FROM estadistiques e INNER JOIN usuaris u ON e.id_usuari = u.id_usuari INNER JOIN partides p ON u.id_usuari = p.id_usuari WHERE u.id_usuari = %s", (id_usuari,))
        sql_estadistiques = cur.fetchone()

        # error de ID no trobat
        if sql_estadistiques is None:
            raise HTTPException(status_code=404, detail="ID_usuari no trobat")

    # error de tipus d'argument
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")

    # si o si tanquem la connexio a la bbdd al final
    finally:
        cur.close()
        conn.close()

    # return del resultat de la query
    return sql_estadistiques