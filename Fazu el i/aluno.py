a = int(input('Escolha uma posição de 1 a 10: '))

lista = ['Maquera', 'Ederson', 'Massa', 'Peron', 'Tannús',
         'Tico', 'Flausino', 'Ana', 'Hai', 'Emiliano']

if 1 <= a <= 10:
    print('Está na lista')
    print(lista[a-1])

else:
    print('Não está na lista, a lista tem apenas 10 pessoas')
