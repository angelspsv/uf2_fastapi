# fitxer per crear la taula
from ACTIVITAT_9.db_connect.conn import *

def create_taula():
    # per fer la connexio s'utilitza el mètode cursor()
    try:
        conn = connection_db()
        cursor = conn.cursor()

        sql = '''CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            nom VARCHAR(20),
            cognom VARCHAR(30),
            edat INTEGER,
            email VARCHAR(50),
            movil VARCHAR(15)
        )
        '''

        # Amb el mètode execute() s'envia la query
        cursor.execute(sql)

        # Commit desar els canvis realitzats de la query a la taula/BD
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # Tancar els recursos manualment
        cursor.close()

