#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

def votacao():
    print("- VOTAÇÕES ABERTAS -")
    print("QUAL JOGO É MELHOR?")
    print("(1) - The Last Of Us\n(2) - Red Dead Redemption \n(3) - God Of War")
    
    tlou = 0
    rd = 0
    gow = 0
    
    while(True):
        voto = int(input("VOTO: "))
        match voto:
            case 1:
                tlou += 1
            case 2:
                rd += 1
            case 3: 
                gow += 1
            case _:
                print("Opção de voto inválida!")
            
        continuar = int(input("Deseja continuar votando?\n(1) - SIM\n(2) - NÃO\n"))
        if(continuar == 2):
            break

    print("\nRESULTADOS:")
    print(f"The Last Of Us: {tlou} votos")
    print(f"Red Dead Redemption: {rd} votos")
    print(f"God Of War: {gow} votos")

votacao()