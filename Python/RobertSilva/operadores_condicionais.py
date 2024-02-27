altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura**2)
imc = round(imc,2)
#print(imc)
if imc >= 16 and imc <= 16.9:
    print('Muito abaixo do peso - {}'.format(imc))
elif imc >= 17 and imc <= 18.4:
    print('Abaixo do peso - {}'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal - {}'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Acima do peso - {}'.format(imc))
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau 1 - {}'.format(imc))
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau 2 - {}'.format(imc))
elif imc >= 40:
    print('Obesidade Grau 3 - {}'.format(imc))
else: 
    print('Padrão não encontrado')
