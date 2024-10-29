#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

def verificadorPalindromo(texto):
    textoFormatado = ''.join(texto.split()).lower()
    return textoFormatado == textoFormatado[::-1]

def mostrarResultados():
    texto = input("Digite uma palavra ou frase: ")
    if(verificadorPalindromo(texto)):
        print(f"A palavra/frase digitada é um palíndromo.")
    else:
        print(f"A palavra/frase digitada não é um palíndromo.")

mostrarResultados()