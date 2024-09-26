import yfinance as yf
import pandas as pd
import time
from datetime import datetime

# Caminho do arquivo CSV
file_path = 'data.csv'

# Tentar carregar os dados existentes do CSV, se o arquivo já existir
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Datetime', 'BTC_in_BRL'])

# Obter o valor do dólar através do código 'BRL=X' (BRL para USD)
dolar_brl = yf.Ticker('BRL=X')
valor_dolar = dolar_brl.history(period='1d')['Close'].iloc[0]

# Obter o valor do Bitcoin em dólares (BTC-USD)
btc = yf.Ticker('BTC-USD')
valor_btc = btc.history(period='1d')['Close'].iloc[0] * valor_dolar

# Obter a data e hora atuais
current_time = datetime.now()

# Criar um novo registro com data e valor do BTC em reais
new_data = pd.DataFrame([[current_time, valor_btc]], columns=['Datetime', 'BTC_in_BRL'])

# Concatenar ao DataFrame existente
df = pd.concat([df, new_data], ignore_index=True)

# Mostrar o DataFrame atualizado
print(df)

# Salvar o DataFrame atualizado no CSV
df.to_csv(file_path, index=False)