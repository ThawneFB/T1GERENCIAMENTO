from calc import somar, subtrair, multiplicar, dividir, potencia, raiz_quadrada

def menu():
    print("=== Calculadora Simples ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if not opcao.isdigit():
        print("Digite apenas números do menu!")
        continue

    if opcao == "0":
        print("Saindo...")
        break

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida!")
        continue

    # Raiz Quadrada só precisa de um número
    if opcao == "6":
        a = float(input("Digite o número: "))
        if a < 0:
            print("Não dá pra calcular raiz de número negativo!")
        else:
            print("Resultado:", raiz_quadrada(a))
        continue

    # Demais operações precisam de dois números
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(a, b))
    elif opcao == "2":
        print("Resultado:", subtrair(a, b))
    elif opcao == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcao == "4":
        if b == 0:
            print("Não dá pra dividir por zero!")
        else:
            print("Resultado:", dividir(a, b))
    elif opcao == "5":
        print("Resultado:", potencia(a, b))
