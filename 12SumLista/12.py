lista = [1, 7, 14, 15, 19, 24, 32, 56]


def soma(lista):
    if not lista:

        return 0
    return lista[0] + soma(lista[1:])


soma = soma(lista)
print(f'A soma é: {soma}')
