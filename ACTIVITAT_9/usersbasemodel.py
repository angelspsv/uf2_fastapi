from pydantic import BaseModel

#BaseModel
class Users(BaseModel):
    nom: str
    cognom: str
    edat: int
    email: str
    movil: str
