import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Bem vindo ao jogos *******")
    print("*********************************")

    print("Qual o jogo que deseja jogar?")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Selecione seu jogo : "))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo ==2):
        print("jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
