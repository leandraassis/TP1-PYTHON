#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

palavraUser = input("Digite uma palavra: ")

def verificadorPalavras(palavra):
    if(len(palavra) >= 5):
        print(f"A palavra {palavra} tem {len(palavra)} letras, portanto é longa")
    else:
        print(f"A palavra {palavra} tem {len(palavra)} letras, portanto é curta")

verificadorPalavras(palavraUser)