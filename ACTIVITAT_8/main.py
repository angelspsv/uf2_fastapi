from fastapi import FastAPI

app = FastAPI()


#endpoint d'exemple GET amb missatge
@app.get("/")
async def root():
    return {"message": "Hello World"}


#endpoint metode GET return item
@app.get("/item/{id_item}")
async def returnItem(id_item):
    return {"id_item": id_item}
