def questão():

    print(' Questão: Qual a capital do Brasil?')
    print('a) São Paulo')
    print('b) Rio de Janeiro')
    print('c) Brasília')
    print('d) Belo Horizonte')


resposta = str(input('Digite sua resposta: '))

if resposta == 'c':
    print('você acertou!')
elif resposta in ['a', 'b', 'd']:
    print('você errou!')
else:
    print("digite qualquer letra entre a e d")

questão()
