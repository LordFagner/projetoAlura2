import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
url = '/home/fagner/projetoAlura/database/TelecomX_Data_com_0_e_1.csv'
# Carregar o JSON


df = pd.read_csv(url)
total_clientes = df['customerid'].count()

total_que_permanesceram = df.query('churn == 0')['churn'].count()
print(total_que_permanesceram)
total_que_sairam = df.query('churn == 1')['churn'].count()
pessaos_que_sairam = df.query('churn == 1')
print(total_que_sairam)
percentul_que_sairam = (total_que_sairam/total_clientes) * 100
percentual_que_ficaram = (total_que_permanesceram/total_clientes) * 100 

homens_que_sairam = (pessaos_que_sairam.query('gender == 2')['customerid'].count() / total_que_sairam) * 100
mulheres_que_sairam = (pessaos_que_sairam.query('gender == 1')['customerid'].count() / total_que_sairam) * 100


fig , sairam_ficaram  = plt.subplots(figsize=(10, 6))
wd,tx,at =  sairam_ficaram.pie([total_que_permanesceram, total_que_sairam], labels=['Permanesceram','Saíram'] , colors= ['r','b'], autopct='%1.1f%%',startangle=90,explode=(0,0.1),shadow=True) 
for color in at : 
    color.set_color('white')
    color.set_fontsize(12)
sairam_ficaram.set_title('Clientes que sairam e que permaneceram na TelecomX', fontsize=20)
sairam_ficaram.text(0,-1.3,'o grafico possui um erro percentual de  + ou - 4% ', fontsize=12, ha = 'center',va = 'top' , color='black')
fig2,ax = plt.subplots(2,2,figsize=(15, 12))

sns.barplot(x=['homens','mulheres'] , y=[homens_que_sairam, mulheres_que_sairam], palette=['blue', 'pink'], ax=ax[0,0])

ax[0, 0].set_title('Percentual de Quem Saiu por Gênero')
ax[0, 0].set_ylabel('Percentual (%)')
ax[0, 0].set_ylim(0, 100)
valores = [homens_que_sairam, mulheres_que_sairam]
for index, value in enumerate(valores):
    ax[0, 0].text(
        index,                          # Posição x (posição da barra)
        value + 2,                      # Posição y (um pouco acima da barra)
        f'{value:.1f}%',                # Texto com 1 casa decimal
        ha='center', fontsize=11, color='black'
    )
ax[0, 1].set_visible(False)  # Desativa se quiser
ax[1, 0].set_visible(False)  # Desativa se quiser
ax[1, 1].set_visible(False)

plt.tight_layout()
plt.show()















"""
como gerei meu arqivo csv editado e normalizado 
# valores de referencia para a criação do grafico
{'Mailed check': 1, 'Electronic check': 2, 'Credit card (automatic)': 3, 'Bank transfer (automatic)': 4}
{'DSL': 1, 'Fiber optic': 2, 'no': 0}
mulher : 1 , homem: 2 

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