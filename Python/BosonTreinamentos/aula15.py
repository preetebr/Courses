#Explicação sobre o conteúdo ELIF

nota1 = 6
nota2 = 8

media = (nota1 + nota2) / 2


if media >= 7:
    print("Aluno aprovado")
    print("Parabéns")
else:
    if media >= 5:
        print('Aluno em recuperação')
    else:
        print("Não aprovado")
        print("Se fudeu")

print("A sua média foi {}".format(media))