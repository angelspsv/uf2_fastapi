from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola Roger!"}


#endpoint metode GET return item
@app.get("/item/{id_item}")
async def returnItem(id_item):
    return {"id_item": id_item}



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


# metode get per llançar excepcio 404
@app.get("/alumne/{id}", status_code=404)
async def mostra_alumne(id):
    return id


# metode get modificat amb response per HTTPException
items = {"2": "dos"}
@app.get("/alumno/{id}")
async def mostra_alumne(id):
    if id not in items:
        raise HTTPException(status_code=404, detail="id not found in items")
    return {"id": items[id]}

