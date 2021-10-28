import random

def jogar():
    print("****************************************")
    print("** Bem vindo ao jogo de Adivinhação! **")
    print("****************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define seu nível: "))

    if (nivel == 1) :
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("******************")
        print(("Tentativa {} de {}".format(rodada, total_de_tentativas)))
        # Comando que recebe o número do usuário
        chute_str = input("Digite o seu número: ")
        # Convertendo o número
        chute = int(chute_str)

        print("Você digitou:", chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100")
            continue

        # Variaveis de condição
        acertou = chute == numero_secreto
        chuteMaior = chute > numero_secreto
        chuteMenor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (chuteMaior):
                print("Você errou o seu chute foi maior que o numero secreto")

            elif (chuteMenor):
                print("Você errou o seu chute foi menor que o numero secreto")
            #Calculo com números absolutos
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("****************************************")
    print("** Fim do jogo **")
    print("Você fez o total de {} pontos".format(pontos))
    print("O número secreto era:", numero_secreto)
    print("****************************************")

if(__name__ == "__main__"):
    jogar()