import requests
import pandas as pd
import matplotlib.pyplot as plt

# chave de acesso

api_key = 'Sua chave aqui'

#buscar uma url

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=GOOGL&apikey={api_key}'

# Fazendo uma requisição à URL 

response = requests.get(url)
data = response.json()

# # convertendo em um DataFrame

df = pd.DataFrame(data['Time Series (Daily)']).T
df.index = pd.to_datetime(df.index)

# Selecionando dados
df = df.loc[df.index > (df.index[0] - pd.Timedelta(days = 30))]


# Calculando a cotação
df['variação'] = (df['4. close'].astype(float) - df['1. open'].astype(float)) / df['1. open'].astype(float)

# Ordenando as ações por maior lucro
df = df.sort_values('variação', ascending = False)

# Selecionando as 10 melhores ações
top_10 = df.head(10)

# visual textual
print(top_10[['variação']])

# visual
top_10["4. close"].astype(float).plot()
plt.show()
