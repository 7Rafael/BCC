from random import randint

exercicio = int(input("Qual exercicio ira testar? :D "))
if exercicio == 1:

    print("Bem vindo ao Calculator Tabaja!!")
    numeroAleatorio1 = randint(1,100)
    numeroAleatorio2 = randint(1,100)
    soma = numeroAleatorio1 + numeroAleatorio2

    print(f"Qual é o resultado para {numeroAleatorio1} + {numeroAleatorio2}")
    resposta = int(input("Insira o resultado: "))

    if (soma == resposta):
        print("aaaacertou!! :D") 
    else:
        print("errouuuu!! >:D")
if exercicio == 2:
    print("Bem vindo ao Calculator Tabaja!! 2.0")
    numeroAleatorio1 = randint(1,10)
    numeroAleatorio2 = randint(1,10)
    choice = randint(0,3)

    op = ["+" , "-", "/","*"]
    op = op[choice]
    

    print(f"Qual é o resultado para {numeroAleatorio1} {op} {numeroAleatorio2}")

    resposta = int(input("Insira o resultado: "))

    if (op == '+'):
        certo = numeroAleatorio1 + numeroAleatorio2
    elif (op == '-'):
        certo = numeroAleatorio1 - numeroAleatorio1
    elif (op == '*'):
        certo = numeroAleatorio1 * numeroAleatorio2
    elif (op == '/'):
        certo = numeroAleatorio1 / numeroAleatorio2
    if (resposta == certo):
        print("ta bala")
    else:
        print("F")
        print(certo)

if exercicio == 3:
    
    a = int(input("insira o primeiro numero: "))
    b = int(input("insira o segundo numero: "))
    c = int(input("insira o terceiro numero: "))

    r = (a + b)**2
    s = (b + c)**2
    d = (r+s)/2
    print(d)

if exercicio == 4:
    idade = int(input("insira a idade: "))
    totalDias = idade * 365
    print(f"o veio(a) tem {totalDias}")

if exercicio == 5:
    idadeTotalDias = int(input("insira a idade em dias: "))
    idadeAno = int(idadeTotalDias / 365)
    idadeMes = int(idadeTotalDias/30 -(idadeAno * 12))
    idadeDias = int(idadeTotalDias - ((idadeMes * 30) + (idadeAno * 365)))
    if (idadeDias < 0):
        idadeDias = idadeDias * -1
    if (idadeMes > 12):
        idadeMes = idadeMes - 12
        idadeAno = idadeAno + 1
    print(f"o veio(a) tem {idadeAno} ano(s), e {idadeMes} mês(es) e {idadeDias} dia(s) :D")
if exercicio == 6:
    TOTALQUILOS = 50
    MULTAPORQUILO = 7
    multa = 0
    execesso = 0
    pesoPeixe =int(input("Pesos do nemo: "))
    if (pesoPeixe> TOTALQUILOS):
        execesso = pesoPeixe - TOTALQUILOS
        multa = execesso * MULTAPORQUILO
    print(f"João pescou: {pesoPeixe}kg de nemo")
    print(f"O excesso de peixes é: {execesso}")
    print(f"João pagara: {multa}")

if exercicio == 7:
    taxaPoluicao = float(input("insira a taxa de poluição: "))
    MAXPOLUICAO = 0.25
    if(taxaPoluicao > MAXPOLUICAO):
        print("grupo 1")
    if(taxaPoluicao > MAXPOLUICAO and taxaPoluicao > 0.4):
        print("grupo 2 tomou-le")
    if(taxaPoluicao > MAXPOLUICAO and taxaPoluicao > 0.5):
        print("Todo mundo vai de F")
    if(taxaPoluicao <= MAXPOLUICAO):
        print("Ta todo mundo safe po kkkk pode relaxar")

if exercicio == 8:
    anosFumando = int(input("quantos anos tu fuma? "))
    cigarrosDia = int(input("quantos cingaro por dia? "))
    precoCigarro = int(input("qual é o preço do classic?"))
    total = ((anosFumando*365) * cigarrosDia) * precoCigarro
    print(f"Para de fumar kkkkkkkkkk tu ja gastou: {total}")

if exercicio == 9:
    MEUNOME = "Rafaer"
    nomeDigitado = input("digita um nome: ")
    if (nomeDigitado == MEUNOME):
        print("NOME CORRETO")
    else:
        print("NOME INCORRETO")

if exercicio == 10:
    VELOCIDADEPERMITIDA = 50
    velocidadeMotorista = int(input("Tava a quantos fio? "))
    if (velocidadeMotorista > VELOCIDADEPERMITIDA and velocidadeMotorista < VELOCIDADEPERMITIDA + 10):
        print("50 pila pra ti pagar >:D") 
    elif (velocidadeMotorista > VELOCIDADEPERMITIDA and velocidadeMotorista < VELOCIDADEPERMITIDA + 30):
        print("100 pila pra ti pagar >:D")
    elif (velocidadeMotorista > VELOCIDADEPERMITIDA):
        print("F pra ti... -200")    
