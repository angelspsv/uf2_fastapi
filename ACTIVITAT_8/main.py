from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hello World"}


#endpoint metode GET return item
@app.get("/item/{id_item}")
async def returnItem(id_item):
    return {"id_item": id_item}


#endpoint que simula l'acces a una bbdd i el retorn de dades d'un alumne
table_names = [{0: "Lluis", "curs": "DAW2B"},
               {1: "Angel", "curs": "DAW2A"},
               {2: "Marta", "curs": "DAM2C"},
               {3: "Joan", "curs": "ASIX2Z"}]

#agafa el id de l'alumne des del navegador
@app.get("/student/{id}")
async def student_info(id):
    #pas de Str a int
    id_alumne = int(id)
    #si l'id existeix mostra el objecte/diccionari alumne
    if (id_alumne > 0) and (id_alumne <= len(table_names)):
        return table_names[id_alumne]
    #si no existeix llancem una excepcio
    else:
        raise HTTPException(status_code=404, detail="Alumne no trobat")


#BaseModel
class Persona(BaseModel):
    name: str
    surname: str
    email: str
    years: int
    telf: int
    city: str | None = None


#fem el endpoint per crear persones amb metode POST
@app.post("/persona/")
async def create_persona(persona: Persona):
    return persona

