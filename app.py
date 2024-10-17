#%%
import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

import os

#%%
def  separador():
    print("=" * 50 + " Separador " + "=" * 50)


#%%
#Gerando o Dicionário de Dados
dicionario_dados = {
    "total_bill": {"descricao": "Valor total da conta antes das gorjetas", "tipo": "quantitativa", "subtipo": "contínua"},
    "tip": {"descricao": "Valor da gorjeta", "tipo": "quantitativa", "subtipo": "contínua"},
    "sex": {"descricao": "Sexo do cliente", "tipo": "qualitativa", "subtipo": "nominal"},
    "smoker": {"descricao": "Se o cliente fuma", "tipo": "qualitativa", "subtipo": "nominal"},
    "day": {"descricao": "Dia da semana", "tipo": "qualitativa", "subtipo" : "nominal"},
    "time": {"descricao": "Período do dia (almoço ou jantar)", "tipo": "qualitativa", "subtipo" : "nominal"},
    "size": {"descricao": "Tamanho do grupo", "tipo": "quantitativa", "subtipo" : "discreta"}
}

print(dicionario_dados)
separador()


#%%
df = pd.read_csv("data/raw/tips.csv")


#Vizualizando informações do dataset
df.info()
separador()

#Removendo valores nulos
df.dropna(inplace=True)

#%%
print(df)
separador()

# %%

