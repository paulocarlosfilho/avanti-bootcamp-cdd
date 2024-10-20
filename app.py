#%%
import pandas as pd
import numpy as np
import pickle
import os

import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

#%%
def  separador():
    print("=" * 50 + " Separador " + "=" * 50)

""""
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
separador()"""


#%%
#Carregando dados online
df2 = pd.read_csv('https://raw.githubusercontent.com/atlantico-academy/datasets/refs/heads/main/tips.csv')
df2 = df2.to_csv('data/raw/tips.csv')
#%%
#Carregando os dados do local
df = pd.read_csv("data/raw/tips.csv")


df
#Vizualizando informações do dataset
df.info()
separador()

#Removendo valores nulos
df.dropna(inplace=True)

#%%
print(df)
separador()

# %%
#Cirando Lebel Enconder
le = LabelEncoder()

#Aplicando o Label Encoder às colunas categóricas
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['time'] = le.fit_transform(df['time'])
df['day'] = le.fit_transform(df['day'])


x = df.drop('tip', axis=1) #Variável Independente

y = df['tip']              #Variável dependente


#Treinando o Modelo
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Correlação entre as variáveis numéricas
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

separador()


#Criando Modelo de Regressão Linear
model = LinearRegression().fit(X_train, y_train)  #Cirando e treinando o modelo


#Fazendo previsões com os dados de teste
y_pred = model.predict(X_test)

print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print("(Linear Regression) Mean Squared Error:", mse)

# Visualizando os resultados (opcional)
plt.scatter(y_test, y_pred)
plt.xlabel("Valores reais")
plt.ylabel("Valores previstos das Gorjetas")
plt.title("Regressão Linear")
plt.show()

separador()

#Árvore de Decisão
# Criando o modelo de árvore de decisão
model = DecisionTreeRegressor(random_state=42)

# Treinando o modelo
model.fit(X_train, y_train)

# Fazendo previsões com os dados de teste
y_pred = model.predict(X_test)

# Calculando o erro quadrático médio (MSE)
mse = mean_squared_error(y_test, y_pred)

print("(Decision Tree) Mean Squared Error:", mse)

separador()

# Boxplot para comparar o valor da gorjeta por sexo
sns.boxplot(x='sex', y='tip', data=df)
plt.show()

