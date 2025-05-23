vetor1 = list(map(float, input(
    "Digite os elementos do primeiro vetor (separados por espaço), exemplo: 1 2 3: ").split()))
vetor2 = list(
    map(float, input("Digite os elementos do segundo vetor: ").split()))

if len(vetor1) != len(vetor2):
    print("Erro: Os vetores devem ter o mesmo tamanho!")
else:

    operacao = input(
        "Escolha a operação (digite 'soma' ou 'multiplicação'): ").strip().lower()

    if operacao == "soma":
        resultado = [a + b for a, b in zip(vetor1, vetor2)]
        print("Resultado da soma:", resultado)
        # testando uma coisa da aula de prog q achei legal...
    elif operacao in ["multiplicação", "multiplicacao"]:
        resultado = [a * b for a, b in zip(vetor1, vetor2)]
        print("Resultado da multiplicação:", resultado)
    else:
        print("Use 'soma' ou 'multiplicação'.")
