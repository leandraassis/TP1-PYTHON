# Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

def combinacaoNomes():
    nome1 = input("Digite o primeiro nome: ")
    nome2 = input("Digite o segundo nome: ")

    if len(nome1) < 3 or len(nome2) < 3:
        return "Os nomes devem ter comprimento suficiente."
    
    concatenando = (nome1[0] + nome1[1] + nome1[2]) + (nome2[-1] + nome2[-2] + nome2[-3])
    return concatenando

print(combinacaoNomes())
