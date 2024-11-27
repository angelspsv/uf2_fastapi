from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}









