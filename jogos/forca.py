import random
import time


def jogar():

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_tentadas = []
    letras_faltando=len(palavra_secreta)
    total_tentativas = len(palavra_secreta) + 5
    enforcou = False
    acertou = False

    imprime_mensagem_abertura()

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_chute(letras_tentadas)
        faz_iteracao(palavra_secreta, chute, letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        total_tentativas-=1

        imprime_mensagem_rodada(letras_faltando, total_tentativas, letras_tentadas, letras_acertadas)
        imprime_imagem_forca(total_tentativas)

        if(total_tentativas==0):

            enforcou=True

        if ("_" not in letras_acertadas):
            enforcou=False
            acertou = True

    imprime_mensagem_finalizacao(palavra_secreta, acertou, enforcou)

###

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("Início do jogo")

###

def carrega_palavra_secreta(nome_arquivo="Lista-de-Palavras.txt", primeira_linha=0):
    lista_palavras = []  # random.choice(arquivo)
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            lista_palavras.append(linha)

    palavra_secreta = lista_palavras[random.randrange(primeira_linha, len(lista_palavras))]
    return palavra_secreta

###

def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista

####

def pede_chute(letras_tentadas):
    while(True):
        chute = input("Qual letra? ")
        if (not chute):
            print("Digite uma letra!")
            continue
        chute = chute[0]
        while (chute[0] == " "):
            print("Digite uma letra!")
            chute = input("Qual letra? ")[0]
        chute = chute.strip()
        chute = chute.upper()
        if (chute in letras_tentadas):
            print("Letra já tentada!")
            continue
        letras_tentadas.append(chute)
        return chute
###

def imprime_mensagem_finalizacao(palavra_secreta,acertou, enforcou): #poderia fazer um for line in arquivo de texto com as mensagens
    if (acertou == True):
        print("Parabéns! Você acertou a palavra: {}".format(palavra_secreta))
        time.sleep(0.5)
        print("       ___________      ")
        time.sleep(0.5)
        print("      '._==_==_=_.'     ")
        time.sleep(0.5)
        print("      .-\\:      /-.    ")
        time.sleep(0.5)
        print("     | (|:.     |) |    ")
        time.sleep(0.5)
        print("      '-|:.     |-'     ")
        time.sleep(0.5)
        print("        \\::.    /      ")
        time.sleep(0.5)
        print("         '::. .'        ")
        time.sleep(0.5)
        print("           ) (          ")
        time.sleep(0.5)
        print("         _.' '._        ")
        time.sleep(0.5)
        print("        '-------'       ")
        time.sleep(0.5)
        print("Fim do jogo")
    if (enforcou == True):
        print("Você foi enforcado! A palavra era '{}'".format(palavra_secreta))
        time.sleep(0.5)
        print("    _______________         ")
        time.sleep(0.5)
        print("   /               \        ")
        time.sleep(0.5)
        print("  /                 \       ")
        time.sleep(0.5)
        print("//                   \/\    ")
        time.sleep(0.5)
        print("\|   XXXX     XXXX   | /    ")
        time.sleep(0.5)
        print(" |   XXXX     XXXX   |/     ")
        time.sleep(0.5)
        print(" |   XXX       XXX   |      ")
        time.sleep(0.5)
        print(" |                   |      ")
        time.sleep(0.5)
        print(" \__      XXX      __/      ")
        time.sleep(0.5)
        print("   |\     XXX     /|        ")
        time.sleep(0.5)
        print("   | |           | |        ")
        time.sleep(0.5)
        print("   | I I I I I I I |        ")
        time.sleep(0.5)
        print("   |  I I I I I I  |        ")
        time.sleep(0.5)
        print("   \_             _/        ")
        time.sleep(0.5)
        print("     \_         _/          ")
        time.sleep(0.5)
        print("       \_______/            ")
        time.sleep(0.5)
        print("Fim do jogo")

###
def imprime_imagem_forca(total_tentativas):

        if (total_tentativas==6):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==5):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==4):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==3):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==2):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==1):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
            print(" |            ")
            print("_|___         ")
            print()

        if (total_tentativas==0):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
            print(" |            ")
            print("_|___         ")
            print()



def imprime_mensagem_rodada(letras_faltando, total_tentativas, letras_tentadas, letras_acertadas):
    print('Ainda faltam acertar {} letras'.format(letras_faltando))
    print("Tentativas restantes: {}".format(total_tentativas))
    print("Letras tentadas: {}".format(letras_tentadas))
    print(letras_acertadas)

###

def faz_iteracao(palavra_secreta, chute, letras_acertadas):
    index = 0

    for letra in palavra_secreta:

        if (chute == letra):
            letras_acertadas[index] = letra
            print("Encontrei a letra {} na posição {}".format(letra, index + 1))
            print(letras_acertadas)
        elif (chute not in palavra_secreta):
            print("A palavra secreta não contém a letra {}".format(chute))
            break

        index += 1
###

if(__name__ == "__main__"):
    jogar()