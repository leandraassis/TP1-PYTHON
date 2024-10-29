#Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.

valorCompra = float(input("Digite o valor da compra (R$): "))

def calculoDesconto(valorCompra):
    desconto = 0
    if(valorCompra > 500):
        desconto = 0.25
    elif(valorCompra > 200):
        desconto = 0.15
    elif(valorCompra > 100):
        desconto = 0.10

    valorDescontado = valorCompra * desconto
    return valorDescontado

def mostrarResultados():
    descontoObtido = calculoDesconto(valorCompra)
    if(descontoObtido != 0):
        valorAtualizado = valorCompra - descontoObtido
        print("\nResultados:")
        print(f"Desconto: R${descontoObtido:.2f}")
        print(f"Valor da compra com desconto aplicado: R${valorAtualizado}")
    else:
        print("A compra não está apta a receber desconto.")

mostrarResultados()

