def multiplicar_vetor_por_escalar(vetor, escalar):
    resultado = [elemento * escalar for elemento in vetor]
    return resultado


vetor = list(map(float, input(
    "Digite os elementos do vetor separados por espaço: ").split()))
escalar = float(input("Digite o escalar: "))

vetor_resultante = multiplicar_vetor_por_escalar(vetor, escalar)
print("Resultado da multiplicação:", vetor_resultante)
