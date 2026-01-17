from typing import Union
from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI() 

usuario = ()

@app.get("/")
def read_root():
    return{"Hello": "World!"}

@app.get("/roupa/{id_roupa}")
def read_roupa(id_roupa: int):
    return{"id_roupa": id_roupa}

@app.post("/roupa/")
def create_roupa(roupa: roupa):
    return roupa