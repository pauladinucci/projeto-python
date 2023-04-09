import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACab6069d38a93b89030a0146641906ed5"
# Your Auth Token from twilio.com/console
auth_token  = "29a178f0c21454fe873e461b019b1f4e"

client = Client(account_sid, auth_token)


#importações no python sempre na parte superior


#ferramenta twilio envia sms pelo python 

#bibliotecas que serão instaladas: pandas, openpyxl (integração do python com excel) e twilio

#para instalar, abrir terminal, em cmd digitar pip install nomedabiblioteca



#passo a passo de solução

# abrir os 6 arquivos em excel

# para cada arquivo verificar se algum valor na coluna vendas é maior que 55 mil 

#se for maior que 55 mil, enviar sms com o nome, o mês e as vendas dele

#caso não seja maior que 55 mil, não fazer nada


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#toda lista do python fica em colchetes

for mes in lista_meses:
    #print(mes) -roda o mês todo
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
#o f e as chaves tornam a tabela dinâmica percorrendo todos os meses
    #print(tabela_vendas) - roda todas as tabelas
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'] .values[0] #para descobrir o vendedor que fez mais de 55mil
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]     #vai mostrar o valor de vendas do vendedor
        #loc faz uma tabela que tem aquele número ou texto que está buscando, usa-se .values[0] para indicar que quer só o valor
        print(f'no mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}') #printa caso encontre alguém com mais de 55 mil
        message = client.messages.create(
            to="+5521xxxxxxxxx", 
            from_="+19592712673",
            body=f'no mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
#este código é retirado do twilio e enviado um sms para meu número indicando qual vendedor fez mais de 55 mil

print(message.sid)
# se algum valor da tabela vendas for maior que 55 mil (o any diz qualquer tabela/valor)
#so imprime se algum valor for, se não, ele entende como falso

#tabela_vendas é uma variável que vai receber o valor da tabela janeiro

#o que está em {} é a variável que vai mostrar ao printar

#para cada mês, execute lista de meses

#para fazer o código aparecer (rodar), clicar com o esquerdo e selecionar "run in python terminal"

#arquivo tem que estar na mesma pasta para funcionar e nome do arquivo tem que estar completo


#for faz um loop para executar o código
#python sempre lê o código de cima para baixo
#após o for, utilizar identação, o que mostra que está dentro do for


#código para enviar sms para meu número através do twilio

