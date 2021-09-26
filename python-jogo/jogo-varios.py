from random import randint
def gerador_de_numeros():
    numero_gerar = randint(1,4)
    return numero_gerar


def primeiro_boss(arg=gerador_de_numeros()):
    if gerador_de_numeros() == 1:
        print("Vc esta sendo perseguido por um Serial Killer vc tem 3 opçoes")
        print()
        op1 = str("Opção 1 : Peque a espada no bau e mate o boss\n")
        op2 = str("Opção 2 : Corra ate a delegacia e tome muito cuidado\n")
        op3 = str("Opção 3 : Va ate uma ponte e salte de la rapido\n")
        print(op1 + op2 + op3)
        escolher = int(input("Digite qual opção vc escolher . exp= 1,2,3 : \n "))

        numero_boss_vida = randint(1,100)
        sua_vida = randint(1,100)
        if escolher == 1:
            print("hnmmm boa escolhaaa agora lute com o boss Boa sorte")
            if sua_vida > numero_boss_vida:
                print()
                print("Boss Morreu vc vençeu pode ir ")
            else:
                print("Vc morreu hahaha")
        elif escolher == 2:
            if sua_vida > numero_boss_vida:
                print("Vc conseguiu chegar a delecacia")
            else:
                print("Vc morreu")
        elif escolher == 3:
            if sua_vida == numero_boss_vida:
                print("Vc conseguiu pular da ponte")
            else:
                print("Vc acabou pulando e se afogou")
        else:
            print("Error digite o numero certo")
primeiro_boss()

def segundo_boss(arg=gerador_de_numeros()):
    if gerador_de_numeros() == 2:
        print("Vc esta sendo perseguido por um Assasino Perigoso demais")
        print()
        op1 = str("Opção 1 : Meu amigo vc esta preso na cadeira com um assasino atras de vc e agora?\n")
        op2 = str("Opção 2 : Opaaa pelo visto e o seu dia de sorte pegue um barco e veja oq aconteçe\n")
        op3 = str("Opção 3 : ai ai Tem um buraco ai ou vc entra nele ou vc morre oq prefere??\n")
        print(op1 + op2 + op3)
        escolher = int(input("Digite qual opção vc escolher . exp= 1,2,3 : \n "))

        numero_boss_vida = randint(1,100)
        sua_vida = randint(1,100)
        if escolher == 1:
            if sua_vida > numero_boss_vida:
                print("Vc conseguiu sair da cadeia e matou o assasino")
            else:
                print("Vc morreu o Assasino foi pego mais conseuiu escapar")
        elif escolher == 2:
            if sua_vida > numero_boss_vida:
                print("Vc conseguiu pegar o barco deu o fora de la ")
            else:
                print("Vc morreu e nao consegui pegar o barco que azar em ")
        elif escolher == 3:
            if sua_vida > numero_boss_vida:
                print("Vc pulou no buraco e conseguiu escapar que sorte nao??")
            else:
                print("Vc morreu hahahah")
        else:
            print("Coloque o numero certo")
segundo_boss()
def terceiro_boss(arg=gerador_de_numeros()):
    if gerador_de_numeros() == 2:
        print("O seu planeta esta sendo invadido por aliens")
        print()
        op1 = str("Aliens Invadiu o seu planeta e agora?\n")
        op2 = str("Opção 1 : Corra e tente salvar o maximo de pessoas possiveis\n")
        op3 = str("Opção 2 : Pegue o machado de thor e tente derrotar os aliens \n")
        print(op1 + op2 + op3)
        escolher = int(input("Digite qual opção vc escolher . exp= 1,2,3 : \n "))

        numero_boss_vida = randint(1,100)
        sua_vida = randint(1,100)

        if escolher == 1:
            if sua_vida > numero_boss_vida:
                print("Vc conseguiuu salvar muitas pessoas agora espere o exercito ")
            else:
                print("Vc morreu salvando as pessoas considere um heroi kkkk")
        elif escolher == 2:
            if sua_vida > numero_boss_vida:
                print("Vc conseguiuu matar os aliens")
            else:
                print("Que azar nem com o machado vc conseguiu")
terceiro_boss()
def numero_errado(nun=gerador_de_numeros()):
    if gerador_de_numeros() >= 4:
        return gerador_de_numeros()
    else:
        pass
numero_errado()