import random as rd
def dicionario(palavra):
    while palavra != 4 and palavra != 5 and palavra != 6:
        palavra = int(input("Tamanho invalido por favor digite um dos numemeros permitidos (4,5 ou 6): "))

    if palavra == 4:
        dicionarioDePalavras = ["vida","casa","auge","saga","medo","ônus","ermo","suma","vovó","mote"]
        palavra_secreta = dicionarioDePalavras[rd.randint(0, 9)]
    elif palavra == 5:
        dicionarioDePalavras = ["juízo","servo","limbo","prosa","forma","presa","falar","viril","ontem","cunho"]
        palavra_secreta = dicionarioDePalavras[rd.randint(0, 9)]
    elif palavra == 6:
        dicionarioDePalavras = ["hábito","apreço","ensejo","embora","ímpeto","eficaz","outrem","ocioso","júbilo","dispor"]
        palavra_secreta = dicionarioDePalavras[rd.randint(0, 9)]

    return palavra_secreta
def boneco(erro):
    bonequinho = ["----------\n|.     ▎\n|.      \n|.    \n|.     ",
                  "----------\n|.     ▎\n|.    😯\n|.    \n|.    ",
                  "----------\n|.     ▎\n|.    😐\n|.    /\n|.    ",
                  "----------\n|.     ▎\n|.    😨\n|.    /|\n|.    ",
                  "----------\n|.     ▎\n|.    😱\n|.    /|\\\n|.    ",
                  "----------\n|.     ▎\n|.    🥶\n|.    /|\\\n|.    /",
                  "----------\n|.     ▎\n|.    🥵\n|.    /|\\\n|.    / \\"]
    return bonequinho[erro]