# Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

def calcularResultado(numero1, numero2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 // n2
    exibirResultados(soma, subtracao, multiplicacao, divisao)

def exibirResultados(soma, subtracao, multiplicacao, divisao):
    print("\n====================")
    print("===  RESULTADOS  ===")
    print("====================\n")
    print(f"SOMA: {soma}")
    print(f"SUBTRAÇÃO: {subtracao}")
    print(f"MULTIPLICAÇÃO: {multiplicacao}")
    print(f"divisao: {divisao}")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

calcularResultado(n1, n2)