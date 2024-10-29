#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

def decisoes():
    print("É noite, seu carro quebrou no meio da estrada. Nos arredores, apenas árvores e floresta densa.")
    escolha1 = int(input("É um lugar deserto, por que você está aqui?\n(1) - Estou indo visitar minha mãe.\n(2) - Estou a caminho de casa.\n(3) - Eu não sei."))
    
    match escolha1:
        case 1:
            escolhaMae1 = int(input("Sua mãe...não é ela que está te chamando?\n(1) - Não tem ninguém me chamando\n(2) - Quem diabos é você?"))
            if(escolhaMae1 == 1):
                print("Vá ver sua mãe...não é por isso que está aqui? Ela te chama na floresta.")
                print("Mesmo que não saiba o porquê, você segue floresta adentro. É fria, escura e você quase não enxerga, mas, em certo momento, passa a escutar a voz de sua mãe.")
                print("Ela está te chamando para comer biscoitos.")
                print("Seguindo a voz, você encontra uma cabana. Ela parece se destoar da floresta, pois passa uma visão quente e aconchegante.")
                escolhaCabana = int(input("Você vai entrar na cabana?\n(1) - Sim\n(2) - Não"))
                if(escolhaCabana == 1):
                    print("Dentro da cabana, você vê sua mãe sorrindo. Ela oferece biscoitos frescos.")
                    print("Mas algo parece estranho. Você percebe que ela não parece exatamente com sua mãe.")
                    escolhaFinal = int(input("Você vai comer os biscoitos?\n(1) - Sim\n(2) - Não"))
                    if(escolhaFinal == 1):
                        print("Você come os biscoitos e, em seguida, sente uma onda de sonolência. Você desmaia.")
                        print("Quando acorda, está preso em um lugar desconhecido.")
                        print("Você não achou nem um pouco estranho sua mãe apaarecer do nada em uma cabana no meio da floresta? Isso se chama BURRICE. Fim de jogo.")
                    else:
                        print("Você recua, suspeitando que algo não está certo. Sua mãe fica irritada.")
                        print("Ela revela sua verdadeira forma e tenta te capturar, mas você consegue fugir da cabana.")
                        print("Você corre pela floresta e encontra o caminho de volta para a estrada. Você está salvo!")
                else:
                    print("Você decide não entrar na cabana e voltar para a floresta.")
                    print("Enquanto caminha, a voz de sua mãe desaparece e você encontra um caminho de volta para a estrada.")
                    print("Você está salvo, mas com um mistério que ficará pra sempre na sua mente.")
                    print("Fm de jogo.")
            elif(escolhaMae1 == 2):
                print("Sou seu amigo, quero te ajudar.")
                escolhaVoce1 = int(input("(1) - Eu nunca te vi na vida.\n(2) - Já falei que não quero sua ajuda."))
                if(escolhaVoce1 == 1):
                    print("Ele sorri e diz: 'Você não precisa se preocupar. Venha, eu tenho uma solução.'")
                    print("Você hesita, mas acaba seguindo-o floresta adentro.")
                    print("Você não sabe onde está, e o estranho continua sorrindo para você.")
                    print("'Não é legal confiar em quem acabou de conhecer, sorte a sua que eu sou um cara legal.'")
                    print("Depois de muito andar, vocês chegam a um hotel na beira da estrada. Você descobre que o nome do estranho é Bob, e fica grato por ele ter te ajudado")
                    print("No fim, ele era mesmo um cara legal. Ele se despede, vai embora e você espera amanhecer no local.\n")
                    print("Por hoje, você está a salvo, mas lembre-se: você só não morreu porque Bob não estava com fome.")
                else:
                    print("Você se recusa a aceitar a ajuda e decide continuar sozinho.")
                    print("A floresta parece mais densa e sombria, mas você não desiste.")
                    print("Após um tempo, você encontra uma estrada e avista um hotel.")
                    print("Você está quase lá, falta pouco para se salvar.")
                    print("Você atravessa a rua para chegar ao hotel.")
                    print("De repente, um clarão atinge seus olhos. Não dá para enxergar nada. Cego, você sente o impacto de um carro contra seu corpo.")
                    print("Você não consegue se mexer, está deitado no chão, sangrando. Não consegue gritar por ajuda.")
                    print("Você ouve o motorista saindo do carro e os passos dele até você.")
                    print("É o homem que te ofereceu ajuda mais cedo.")
                    print("'Bob só queria um amigo. Você não deveria ter sido tão cruel com Bob.'\n")
                    print("Bob te matou. Fim de jogo.")
            else:
                print("Você não está cooperando...vamos ter que te eliminar. Achem outra cobaia.")
                print("Fim de jogo. Você foi eliminado.")
        
        case 2:
            print("Ah, sim. Tenho umas ferramentas em casa, se quiser te empresto para que possa consertar o carro, o que acha?")
            print("Você não quer ir, mas não tem outra opção.")
            print("*Você o segue floresta adentro até a casa dele. A cabana é meio macabra, mas é bom sair do frio.*")
            print("Fique aqui, vou pegar as ferramentas.")
            escolhaCasa = int(input("Enquanto você espera, você ouve barulhos estranhos. O que você faz?\n(1) - Investigar os barulhos\n(2) - Ficar quieto"))
            if(escolhaCasa == 1):
                print("Você se aproxima da origem do som, ele leva a um lugar: o porão.")
                print("Assim que você entra no porão, a porta atrás de você é fechada com força. Tudo está escuro. Não há luz.")
                print("'Finalmente...' Uma voz monstruosa murmura. 'Pensei que ele não fosse me alimentar hoje.'")
                print("Você nunca ouviu o ditado 'A curiosidade matou o gato?' Que burrice! Fim de jogo.")
            else:
                print("Você decide ficar quieto e esperar. Após um tempo, ele retorna com as ferramentas.")
                print("Você consegue consertar seu carro e parte em segurança. Você está salvo!")
        
        case 3:
            print("Você está perdido? Posso te ajudar.")
            escolhaNaoSei1 = int(input("(1) - Como?\n(2) - Não quero sua ajuda."))
            if(escolhaNaoSei1 == 1):
                print("Fazendo você se lembrar do porquê está aqui.")
                print("Você tenta se lembrar, mas as memórias são confusas.")
                print("O estranho se aproxma e diz: 'Apenas continue andando, confie em mim.'")
                print("Você decide confiar nele e segue em frente, mas se perde ainda mais na floresta.")
                print("Após horas vagando, você desmaia de exaustão.")
                print("A vida não é um filme, aquele cara fugiu do hospicio. Não confie em qualquer maluco que vê pela frente. Fim de jogo.")
            elif(escolhaNaoSei1 == 2):
                print("Eu sou sua única opção, está vendo mais alguém aqui?")
                print("Você percebe que ele está certo. Você não confia nele, mas está sem alternativas.")
                print("O estranho usa uma roupa desgastada e tem um olhar estranho, mas mesmo assim o acompanha.")
                print("Enquanto caminha, você mantém uma distância segura, observando cada movimento dele.")
                print("Após um tempo, você vê luzes de faróis e escuta sons de carros à distância.")
                print("O estranho aponta para a estrada e diz: 'Lá está a saída.'")
                print("Você se despede do estranho e corre em direção à estrada.")
                print("Finalmente, você consegue parar um carro que passa e é resgatado.")
                print("Você sobreviveu, e até hoje não entende o porquê. Tempos depois você descobriu que aquele cara era um serial killer, por quê ele não te matou? Acho que nunca saberemos.")
            else:
                print("Por quê você simplesmente não seguiu o fluxo e brincou direito? Não queria ter que fazer isso com você.")
                print("Fim de jogo. Você morreu.")
        case _:
            print("Você não pode escolher isso...eu já não te disse? Essas são suas únicas opções.")
            print("Essa teimosia ainda vai te matar.\n")
            print("E matou mesmo. Fim de jogo.")

decisoes()