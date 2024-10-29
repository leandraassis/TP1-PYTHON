# Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, combine-os para formar uma saudação personalizada.

def cumprimentoPersonalizado():
    nome = input("Olá, por favor, digite seu primeiro nome: ")
    sobrenome = input("Agora, digite seu sobrenome: ")
    return f"Seja bem vindo(a), {nome} {sobrenome}!"

print(cumprimentoPersonalizado())