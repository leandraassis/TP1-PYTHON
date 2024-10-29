#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random 

qtdDados = int(input("Quantos dados você deseja jogar?"))

def resultados(qtd): 
    print("RESULTADOS:")
    for i in range(1, qtd + 1):
        dadoResult = random.randint(1, 6)
        print(f"Dado {i}: {dadoResult}")

resultados(qtdDados)