import pandas as pd
import numpy as np
url = '/home/fagner/projetoAlura/database/TelecomX_Data_Normalizado.csv'
# Carregar o JSON
df = pd.read_csv(url)

"""colunas_binarias = [col for col in df.columns 
                     if set(df[col].dropna().astype(str).str.lower().unique()) <= {'yes', 'no'}]


df[colunas_binarias] = df[colunas_binarias].apply(lambda x: x.str.lower().map({'yes': 1, 'no': 0}))

df.to_csv('/home/fagner/projetoAlura/database/TelecomX_Data_Normalizado.csv')
"""

"""
colunas_com_no = [col for col in df.columns 
                   if 'no' in set(df[col].dropna().astype(str).str.lower().unique())]

colunas_com_no = [col for col in colunas_com_no if col != 'churn']  # Excluindo a coluna 'Churn' se estiver presente

df[colunas_com_no] = df[colunas_com_no].applymap(lambda x: 0 if str(x).strip().lower() == 'no' else 1)"""

df['churn'] = df['churn'].apply(lambda x: 1 if str(x).strip().lower() != 'no' else 0)
df.to_csv('/home/fagner/projetoAlura/database/TelecomX_Data_com_0_e_1.csv')













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

"""  
customerID: número de identificação único de cada cliente
Churn: se o cliente deixou ou não a empresa
gender: gênero (masculino e feminino)
SeniorCitizen: informação sobre um cliente ter ou não idade igual ou maior que 65 anos
Partner: se o cliente possui ou não um parceiro ou parceira
Dependents: se o cliente possui ou não dependentes
tenure: meses de contrato do cliente
PhoneService: assinatura de serviço telefônico
MultipleLines: assisnatura de mais de uma linha de telefone
InternetService: assinatura de um provedor internet
OnlineSecurity: assinatura adicional de segurança online
OnlineBackup: assinatura adicional de backup online
DeviceProtection: assinatura adicional de proteção no dispositivo
TechSupport: assinatura adicional de suporte técnico, menos tempo de espera
StreamingTV: assinatura de TV a cabo
StreamingMovies: assinatura de streaming de filmes
Contract: tipo de contrato
PaperlessBilling: se o cliente prefere receber online a fatura
PaymentMethod: forma de pagamento
Charges.Monthly: total de todos os serviços do cliente por mês
Charges.Total: total gasto pelo cliente

"""