import forca
import adivinhacao

def escolhe_jogo():
    print("****************************************")
    print("** Bem vindo aos jogos em python! **")
    print("****************************************")
    print("** Escolha seu jogo! **")
    print("****************************************")

    print("Selecione o jogo")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?: "))

    if(jogo == 1):
        print("Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhacao")
        adivinhacao.jogar()
    else:
        print("jogo nao encontrado")
        return escolhe_jogo()

if(__name__ == "__main__"):
    escolhe_jogo()