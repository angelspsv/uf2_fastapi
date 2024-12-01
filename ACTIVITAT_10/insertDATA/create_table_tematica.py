#importem fitxer per crear la taula
from connection import *


def create_taula():
    # per fer la connexio utilitzem el mètode cursor()
    try:
        conn = connection_db()
        cursor = conn.cursor()

        sql = '''CREATE TABLE IF NOT EXISTS tematicas(
            id SERIAL PRIMARY KEY,
            word VARCHAR(50),
            theme VARCHAR(50)
        )
        '''

        # Amb el mètode execute() s'envia la query per crear la taula
        cursor.execute(sql)

        # Commit desar els canvis realitzats de la query a la taula/BD
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # Tancar els recursos manualment
        cursor.close()


#create_taula()