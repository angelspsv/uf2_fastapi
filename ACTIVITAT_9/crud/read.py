from db_connect.conn import *

#metode read per consultar les entrades a la taula users de la bbdd
def read_users():
    try:
        conn = connection_db()
        cur = conn.cursor()

        sql_read = '''SELECT * FROM users'''

        # Amb el mètode execute() s'envia la query
        cur.execute(sql_read)
        users = cur.fetchall()

    except Exception as e:
        return {"message": f"Error de connexió:{e}"}

    finally:
        conn.close()

    return users