import pandas as pd
url = '/home/fagner/projetoAlura/database/TelecomX_Data_Normalizado.csv'
# Carregar o JSON
df = pd.read_csv(url)
print(df.head())
"""
como gerei meu arqivo csv editado e normalizado 

print('--'*50)
# Normalizar o JSON
internet_normalizado = pd.json_normalize(df['internet'])
account_normalizado = pd.json_normalize(df['account'])
customer_normalizado = pd.json_normalize(df['customer'])
phone_normalizado = pd.json_normalize(df['phone'])
# Se quiser, pode agora definir o índice

firstpart = df[['customerID','Churn']]

df_normalizado = pd.concat([firstpart,internet_normalizado, account_normalizado, customer_normalizado, phone_normalizado], axis=1)

df_normalizado.to_csv('/home/fagner/projetoAlura/database/TelecomX_Data_Normalizado.csv', index=False)
print(df_normalizado.head())

"""