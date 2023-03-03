from enum import Enum
exercicios = int(input("qual exercicio tens interesse meu consagrado? "))

if exercicios == 1 :
    sexoJogador = input("sexo kkkkkkkkk do jogador? M ou F ")
    pontosJogador = int(input("Quantos pontos fu fez? "))
    sexoF = 0.07
    sexoM = 0.05
    pontos = 0
    if sexoJogador == "M":
        pontos = pontosJogador * sexoM
    else:
        pontos = pontosJogador * sexoF
    print(pontos)

if exercicios == 2 :
    idadeJogador = int(input("qual tua idade fio? "))
    IDADEMIN = 16

    if idadeJogador > IDADEMIN:
        print("pode jogar fio, cuidado 0_0")
    else:
        print("F pra ti, pode jogar n...")

if exercicios == 3 :

    numMoedaOuro = int(input("\t1 - Ouro: "))
    numMoedaPrata = int(input("\t2 - Prata: "))
    numMoedaBronze = int(input("\t3 - Bronze: "))

    converterMoeda = input("Para qual moeda quer converter? ")
    if converterMoeda == "Ouro":
        print("vamo converter para ouro")
    elif converterMoeda == "Prata":
        print("vamo converter para prata")
    elif converterMoeda == "Bronze":
        print("vamo converter para Bronze")
        ouro = numMoedaOuro * 50
        prata = (ouro + numMoedaPrata) * 50
        bronze = prata + numMoedaBronze
        print(bronze)


    