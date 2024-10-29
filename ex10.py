#Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.

import random 

personagens = ["Grávida de Taubaté", "Ken humano", "Harbor", "Gekko", "Killjoy", "Raze", "Sova", "Miss Fortune", "Bob Esponja", "Timmy Turner"]
personagensDois = ["Lula Molusco", "Patrick Estrela", "Wandinha gótica", "Papai Pig", "Peppa Pig", "Galinha Pintadinha", "Shrek", "Garfield", "Márcia Sensitiva", "Homem-Aranha"]
acoes = ["matou", "socou", "empurrou", "beijou", "chutou", "abraçou", "leu um livro com", "dançou com", "cuspiu em", "xingou"]
lugares = ["dentro de casa", "em Xique-Xique, Bahia", "no Rio de Janeiro", "em Ribeirão Preto", "em Bangu", "na casa da Taylor Swift", "dentro de um bueiro", "em Niterói", "em Plutão", "na esquina"]

def historia():
    p1 = random.randint(0, len(personagens) - 1)
    p2 = random.randint(0, len(personagensDois) - 1)
    acao = random.randint(0, len(acoes) - 1)
    lugar = random.randint(0, len(lugares) - 1)
    print(f"{personagens[p1-1]} {acoes[acao-1]} {personagensDois[p2-1]} {lugares[lugar-1]}.")

historia()
