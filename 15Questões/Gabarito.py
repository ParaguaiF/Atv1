gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']

print('Digite as repostas para cada questão: ')

respostas = []

for i in range(1, 11):

    while True:

        resposta = input(f'Questâo {i}: ').upper()
        if resposta in ['A', 'B', 'C', 'D']:
            respostas.append(resposta)
            break
        else:
            print('Digite as letras A, B, C ou D')

    acertos = 0
for i in range(10):
    if gabarito[i] == respostas[i]:
        acertos += 1

print('\nResultado: ')
print(f'Gabarito: {gabarito}')
print(f'Respostas: {respostas}')
print(f'Acertos: {acertos}')
