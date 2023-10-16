from funcoes import *
from unidecode import unidecode
jogarNovamente = "s"
while jogarNovamente in "sS":
    letras_acertadas = []
    letras_testadas = []

    palavra = int(input("====================\n  JOGO DA FORCA \n====================\nEscolha o nivel de dificuldade entre 4 e 6\n----------\n|.     ▎\n|. 4- palavras com 4 letras (facil)      \n|. 5- palavras com 5 letras (medio)   \n|. 6- palavras com 6 letras (dificil)    \n====================\n"))

    palavra_chave = dicionario(palavra)


    for i in palavra_chave:
        letras_acertadas += '_'

    erros = 0
    print(letras_acertadas)

    while True:
        print(boneco(erros))
        letra = input("Digite uma letra: ").lower()

        if letra not in 'abcdefghijklmnopqrstuvwxyz':
            print("por favor digite uma letra entre a-z")
            continue

        if len(letra) > 1:
            print("Você digitou mais de uma letra")
            continue

        if letra in letras_testadas:
             print("Você já tentou utilizar essa letra.")

        else:
            letras_testadas += letra
            if letra in unidecode(palavra_chave):
                for x in range(len(palavra_chave)):
                    if letra == unidecode(palavra_chave[x]):
                        letras_acertadas[x] = palavra_chave[x]

            else:
                erros += 1

        print(f"Você acertou a(s) seguinte(s) letras: {letras_acertadas}   ", end='')
        print(f'Letras usadas: {letras_testadas}')

        if "".join(letras_acertadas) == palavra_chave:
            print("     \n    😎৲ \n    /|┙\n    / \\")
            jogarNovamente = input(f"Você ganhou!!! a palavra era {palavra_chave}, deseja jogar novamente(digite S para jogar novamente)? ")
            break
        if erros == 6:
            print(boneco(erros))
            jogarNovamente = input("Você perdeu, deseja jogar novamente(digite S para jogar novamente)? ")
            break