from random import randint
import time


# ESTE E O JOGO EM SI

def jogo():
    print("Jogo de adivinha \n "
    "Chute um numero de  1 a 10")

    print()

    numero_entre  = numero = randint(1, 10)
    usuario_numero = int(input("Digite o numero :"))
    if usuario_numero == numero_entre:
        print("Vc acertou o numero é : {}".format(numero_entre))
        print()
        return jogar_novamente()
    elif usuario_numero > 10:
        print()
        print("Porfavor nao tente colocar um numero acima de 10 Olhe a regra do jogo")
        print()
        return jogo()
    else:
        print("Vc errou")
        print()
        return jogar_novamente()

# ESTE E UM METODO QUE REPETE O JOGO DE NOVO

def jogar_novamente():
    jogar_de_novo = str(input("Digite [s] para jogar novamente ou [n] para sair : "))
    print()
    jogar = jogar_de_novo.upper()
    if jogar == "S":
        return iniciar()
    elif jogar == "N":
        print("Jogo sendo fechado porfavor aguarde 30segundos")
        time.sleep(30)
        exit()
    else:
        print("Escreveu errado porfavor esscreva corretamente")


# ESTE E O INICIAR DO JOGO OU SEJA O LOBBY KKKK

def iniciar():
    print("Bom este e um jogo criado para fazer vc passar raiva kkk nao tem outro motivo\n"
          "Espero que goste do jogo nao deu trabalho pra fazer para falar  a verdade \n "
          "apenas vi no yt jogo para fazer exercicios ai apareçeu entao kkk e isso")
    print()


    iniciar_game = str(input("Digite [Jogar] PARA Iniciar o Game, Ou Digite [Sair]:  : \n"))
    print()
    iniciar_game = iniciar_game.upper()
    if iniciar_game == "JOGAR":
        return jogo()
    elif iniciar_game == "SAIR":
        exit()
    else:
        print()
        print("Porfavor Digite O nome Correto")
iniciar()