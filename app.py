import math

a = float(input('Dgite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Dgite o valor de c: '))

d = b ** 2 - 4 * a * c

if d >= 0:
    x = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
else:
    print("não tem raízes reais")
    exit()
print(x)
print(x2)
