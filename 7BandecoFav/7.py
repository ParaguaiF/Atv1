def fav():

    print('Escolha a sua opção favorita do bandeco:')
    print('\n1 - Brigadeirão')
    print('2 - Aborgue')
    print('3 - Peixe')
    print('4 - Fricassê de Frango')
    print('5 - Lasanha')

    try:

        escolha = int(input('\nQual seu Bnadeco favorito? Digite de 1 a 5: '))

        bandecos = {
            1: "Brigadeirão",
            2: "Aborgue",
            3: "Peixe",
            4: "Fricassê de Frango",
            5: "Lasanha"
        }

        if 1 <= escolha <= 5:
            print(f'\nvocê escolheu: {bandecos[escolha]}')
        else:
            print('\nPor favor, digite um número de 1 a 5')
            print('\nObrigado por participar :)')

    except ValueError:
        print('\nErro: Digite um número entre 1 e 5')
        print('\nObrigado por participar :)')


fav()
