import psycopg2


def connection_db():
    conn = psycopg2.connect(
        database="mydatabase",
        user="admin",
        password="admin",
        host="localhost",
        port="5432"
    )

    print("Connexió establerta correctament")
    return conn