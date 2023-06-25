from fastapi import FastAPI

import pandas as pd 
import json
app = FastAPI()

@app.get("/home")
def home():
    dados = pd.read_excel("teste.xlsx")    
    dados = dados.to_json(orient="records")
    dados = json.loads(dados)
    return dados
