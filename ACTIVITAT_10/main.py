import pandas as pd


#funcio que llegeix el fitxer csv i retorna una llista per un insert a la bbdd
def deCsvALista():
    #es crea el dataframe
    df = pd.read_csv("paraules_tematica_penjat.csv")
    #fem una llista a partir del dataframe
    llista_dades = df.values.tolist()
    #retornem la llista generada
    return llista_dades


