


compra_confirmada = True
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Dados enviados por email')
        break
else:
    print('Falha na compra')