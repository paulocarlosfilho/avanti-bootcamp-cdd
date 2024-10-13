#%%
import pandas as pd
import os

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

dicionario_dados
#%%
df = pd.read_csv("data/raw/tips.csv")


#Vizualizando informações do dataset
df.info()

#Removendo valores nulos
df.dropna(inplace=True)

#%%
df