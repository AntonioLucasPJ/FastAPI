from fastapi import FastAPI
from flask import jsonify
import pandas as pd 
import json
app = FastAPI()

@app.get("/home")
def home():
    tabela = pd.read_excel("teste.xlsx")    
    tabela = tabela.to_json(orient="records")
    return tabela
