#Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

import random 

def gerarNumero():
    numeroGerado = random.randint(1, 100)
    return numeroGerado

def verificaNumero(numeroGerado):
    while(True):
        numeroEscolhido = int(input("Adivinhe o número: "))
        if(numeroEscolhido > numeroGerado):
            print("Palpite está muito alto!")
        elif(numeroEscolhido < numeroGerado):
            print("Palpite está muito baixo!")
        else:
            print("É isso! Você acertou o número, parabéns!")
            break

def mostraResultados():
    numeroGerado = gerarNumero()
    print("Bem vindo(a) ao jogo de adivinhações!")
    print("Escolhemos um número entre 1 e 100, e você terá que adivinhar que número é esse.\nNão se preocupe, te daremos dicas pelo caminho.")
    print("Vamos começar!\n\n")
    verificaNumero(numeroGerado)

mostraResultados()