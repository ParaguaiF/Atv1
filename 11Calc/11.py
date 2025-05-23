def calculadora(
):

    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potenciação")
        print("0 - Sair")

        try:
            opcao = int(input("\nEscolha uma operação (0-5): "))

            if opcao == 0:
                print("Encerrando a calculadora...")
                break

            if opcao not in range(1, 6):
                print("Opção inválida! Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")

            elif opcao == 2:
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")

            elif opcao == 3:
                resultado = num1 * num2
                print(f"\nResultado: {num1} × {num2} = {resultado}")

            elif opcao == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} ÷ {num2} = {resultado}")

            elif opcao == 5:
                resultado = num1 ** num2
                print(f"\nResultado: {num1} ^ {num2} = {resultado}")

        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


calculadora()
