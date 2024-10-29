#Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

def verificadorIdade():
    idade = int(input("Digite sua idade: "))
    if(idade >= 18):
        return f"Usuário tem {idade} anos, portanto é MAIOR de idade."
    else:
        return f"Usuário tem {idade} anos, portanto é MENOR de idade."

print(verificadorIdade())