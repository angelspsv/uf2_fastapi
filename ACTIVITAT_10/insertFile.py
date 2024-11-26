from connection import *

#fem la funcio que fara l'insert a la taula tematicas
def insert_into_tematica(llista_dict):
    #obtenim la connexio
    conn = connection_db()
    cur = conn.cursor()

    #preparem la query insert
    insert_query = "INSERT INTO tematicas (word, theme) VALUES (%s, %s)"

    try:
        #inserim les dades a la taula tematicas i després desem
        cur.executemany(insert_query, llista_dict)
        conn.commit()

    except Exception as e:
        print(f"Error al inserir les dades: {e}")
    finally:
        cur.close()
        conn.close()