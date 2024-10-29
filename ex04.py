# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

def recebendoNumeros(): 
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    return [num1, num2]

def operacaoEscolhida():
    operacao = int(input("Digite a operação desejada conforme os números:\n(1) - Adição\n(2) - Subtração\n(3) - Multiplicação\n(4) - Divisão\n"))
    return operacao

def calculo(numeros, operacao):
    numero1 = numeros[0]
    numero2 = numeros[1]
    match operacao:
        case 1:
            return numero1 + numero2
        case 2: 
            return numero1 - numero2
        case 3:
            return numero1 * numero2
        case 4: 
            if(numero2) == 0 :
                return "Erro: não há como dividir por zero"
            else:
                return numero1 / numero2
        case _:
            return "Operação inválida!"
        
def mostrandoResultados():
    operacao = operacaoEscolhida()
    numeros = recebendoNumeros()
    resultado = calculo(numeros, operacao)
    print(f"Resultado: {resultado}")

mostrandoResultados()