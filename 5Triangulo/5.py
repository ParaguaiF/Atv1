a = float(input('Digite um valor para o primeiro lado dotriângulo: '))
b = float(input('Digite um valor para o segundo lado dotriângulo: '))
c = float(input('Digite um valor para o terceiro lado dotriângulo: '))

if a == b and b == c:
    print('Seu triângulo é equilátero!')
elif a == b and b != c or a == c and c != b or b == c and c != a:
    print('Seu triângulo é isósceles')
else:
    print('Seu triânculo é escaleno')
