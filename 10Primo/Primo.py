def primo(num):

    if num < 2:

        return False

    for i in range(2, int(num**0.5)+1):

        if num % i == 0:
            return False
    return True


def contarprimos(n):
    contador = 0
    while n >= 2:
        if primo(n):
            contador += 1
        n -= 1
    return contador


try:
    numero = int(input("Digite um número inteiro: "))
    if numero < 2:
        print("Não existem primos abaixo de 2")
    else:
        total = contarprimos(numero)
        print(f'Existem {total} números primos até {numero}')
except ValueError:
    print("Digite só números inteiros")
