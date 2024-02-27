#Modelos de hora e data no python 


#importas módulos datetime e suas classes

from datetime import date, time, timedelta, datetime


#data e hora atuais
current_dateTime = datetime.utcnow()

print(current_dateTime)


#Mostrar o mês de uma data
data_hora = datetime(2019,10,31)
print(data_hora.strftime('%B'))

#Mostrar data e hora atuais com métodos today() e now()
hoje = date.today().strftime('%d/%m/%Y')
agora = datetime.now().strftime('%d/%m/%Y %H:%M')
print("Dia de hoje:", hoje)
print("Data e hora atuais:", agora)


#Data e hora formatos
data_hora = datetime.now().strftime('%d/%m/%Y/ %H:%M')
print(data_hora)


#Mostrar o ano atual e o nome do dia da semana
data_hora = datetime.now()
print(data_hora.year)
print(data_hora.strftime("%A"))

#Criar um objeto de data 

data_hora = datetime(2022,7,10)
print(data_hora)

#Criar um objeto de hora
hora = time(hour=12, minute=15, second=20)
print(hora)

#Transformar string em data: método strptime
data_texto = '11/05/2021'
data_hora = datetime.strftime(data_hora, '%d/%m/%Y')
print(data_hora)

#Mostrar hora UTC
hora_atual = datetime.utcnow().strftime('%H:%M')
print(hora_atual)


#Quantos dias faltam para meu aniversário
meu_aniversario = datetime(year=2024, month=2, day=23, hour=14)
contagem = meu_aniversario -datetime.now()
print(f'Faltam {contagem.days} dias para o seu aniversário!')

#Criar objeto data a partir de uma string com método fromisoformat()
data = date.fromisoformat('2022-07-13')
print(data.strftime('%d/%m/%Y'))


#Adicionar dias a uma data: que dia será daqui a 10 dias?
data_futura = datetime.today() + timedelta(days=10)
print(data_futura.strftime('%d/%m/%Y'))


#módulo dateutil
#data daqui a 3 anos, 2 meses e 10 dias
#necessário instalar o módulo pip install python-dateutil
from dateutil.relativedelta import relativedelta

data_atual = datetime.today()
delta = relativedelta(years=+3, months=+2, days=+10)
data_futura = data_atual + delta
print(data_futura.strftime('%d/%m/%Y'))

#que dia era há 180 dias atrás?
data_passada = datetime.today() + timedelta(days=-180)
print(data_passada.strftime('%d/%m/%Y'))


