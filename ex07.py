#Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

def calcularIMC():
    peso = float(input("Digite seu peso (em quilograma): "))
    altura = float(input("Digite sua altura (em metros): "))
    imc = peso / (altura * altura)
    return imc

def feedback(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
def mostrarResultados():
    imc = calcularIMC()
    situacao = feedback(imc)
    print(f"\nSeu índice de massa corporal (IMC): {imc:.2f}")
    print(f"Situação atual: {situacao}")

mostrarResultados()