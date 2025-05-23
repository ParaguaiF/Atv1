numero = int(input('Digite seu número: '))

try:
    for i in range(numero+1):
        print(i)
except ValueError:
    print('Digite um número decente hahaha :)')
