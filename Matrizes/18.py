linhas_A = int(input("Digite o número de linhas da matriz A: "))
colunas_A = int(input("Digite o número de colunas da matriz A: "))
matriz_A = []
print("Digite os elementos da matriz A linha por linha e separados por espaço:")
for i in range(linhas_A):
    while True:
        linha = input(f"Linha {i+1}: ").split()
        if len(linha) == colunas_A:
            try:
                linha = [float(x) for x in linha]
                matriz_A.append(linha)
                break
            except ValueError:
                print("Erro digite apenas números")
        else:
            print(f"Erro você deve digitar exatamente {colunas_A} elementos!")

# Criar matriz B
linhas_B = int(input("\nDigite o número de linhas da matriz B: "))
colunas_B = int(input("Digite o número de colunas da matriz B: "))
matriz_B = []
print("Digite os elementos da matriz B linha por linha, separados por espaço:")
for i in range(linhas_B):
    while True:
        linha = input(f"Linha {i+1}: ").split()
        if len(linha) == colunas_B:
            try:
                linha = [float(x) for x in linha]
                matriz_B.append(linha)
                break
            except ValueError:
                print("Erro digite apenas números!")
        else:
            print(f"Erro você deve digitar exatamente {colunas_B} elementos!")

print("\nMatriz A:")
for linha in matriz_A:
    print(" ".join(f"{x:6.2f}" for x in linha))
print("\nMatriz B:")
for linha in matriz_B:
    print(" ".join(f"{x:6.2f}" for x in linha))

while True:
    operacao = input(
        "\nEscolha a operação (soma, subtração, multiplicação): ").lower()
    if operacao in ["soma", "subtração", "subtraçao", "subtracao"]:
        if linhas_A != linhas_B or colunas_A != colunas_B:
            print(
                "Erro: Para soma ou subtração, as matrizes devem ter as mesmas dimensões!")
            continue

        resultado = []
        for i in range(linhas_A):
            linha_resultado = []
            for j in range(colunas_A):
                if operacao.startswith("soma"):
                    linha_resultado.append(matriz_A[i][j] + matriz_B[i][j])
                else:
                    linha_resultado.append(matriz_A[i][j] - matriz_B[i][j])
            resultado.append(linha_resultado)

        print(
            f"\nResultado da {'soma' if operacao.startswith('soma') else 'subtração'}:")
        for linha in resultado:
            print(" ".join(f"{x:8.2f}" for x in linha))
        break

    elif operacao in ["multiplicação", "multiplicacao"]:
        if colunas_A != linhas_B:
            print(
                "Erro: Para multiplicação, o número de colunas de A deve ser igual ao número de linhas de B!")
            continue

        resultado = []
        for i in range(linhas_A):
            linha_resultado = []
            for j in range(colunas_B):
                soma = 0
                for k in range(colunas_A):
                    soma += matriz_A[i][k] * matriz_B[k][j]
                linha_resultado.append(soma)
            resultado.append(linha_resultado)

        print("\nResultado da multiplicação:")
        for linha in resultado:
            print(" ".join(f"{x:8.2f}" for x in linha))
        break
    else:
        print("Operação inválida! Escolha entre: soma, subtração ou multiplicação")
