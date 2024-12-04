from fastapi import FastAPI

app = FastAPI()

#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hola!"}