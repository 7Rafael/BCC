"""
Operações matemáticas
Como trabalhar com operadores
14/02/2023
Programa_002.py
"""


from cmath import pi


print(3,5)
if  __name__ == "__main__":
    
    exercicios = int(input("qual exercicio ira ver? "))
    if exercicios == 0:   
        print ("7 + 3= ", 7+3)
        print ("7 - 3= ", 7-3)
        print ("7 * 3= ", 7*3)
        print ("7 / 3= ", 7/3)
        print ("7 + 3 * 5 = ", 7+3*5)
        print ("(7 + 3) * 5 = ", (7+3)*5)
    if exercicios == 1:
        valor1 = int(input("Insira o valor A: "))##pega o valor inserido pelo usuário
        valor2 = int(input("Insira o valor B: "))##pega o valor inserido pelo usuário
    
        copiaValor1 = valor1 ## cópia
        copiaValor2 = valor2 ## cópia
        valor2 = copiaValor1 ## altera o valor
        valor1 = copiaValor2 ## altera o valor
        print(f"o valor de A agora é {valor1}")
        print(f"o valor de B agora é {valor2}")
    if exercicios == 2:
        N1 = float(input("Insira o valor N1: "))##pega a nota inserido pelo usuário
        N2 = float(input("Insira o valor N2: "))##pega a nota inserido pelo usuário
        N3 = float(input("Insira o valor N3: "))##pega a nota inserido pelo usuário
        N4 = float(input("Insira o valor N4: "))##pega a nota inserido pelo usuário
        media = ((N1 + N2*2 + N3*3 + N4*4)/10)

        print(media)
    if exercicios == 3:
        
        distancia = int(input("Insira o valor em metros: "))##pega a nota inserido pelo usuário
        diasTrabalho = int(input("Insira o valor de dias trabalhados: "))##pega a nota inserido pelo usuário
        semPorAno = int(input("Insira o valor semanas no ano: "))##pega a nota inserido pelo usuário
        distanciaPorAno = distancia * diasTrabalho * 2 * semPorAno
        print(f"andou {distanciaPorAno} metros")

    if exercicios == 4:
        montrosNome = ["Feio", "muito feio" ,"horrível"]
        monstrosPontos = [1 , 5, 10]
        monstroFeioMorto = int(input("Quantos monstros feios tu matou? "))
        monstroMuitoFeioMorto = int(input("Quantos monstros muito feios tu matou? "))
        monstroHorrivelMorto = int(input("Quantos monstros horrível tu matou? "))

        
        totalPontos = float((monstrosPontos[0] * monstroFeioMorto) + (monstroMuitoFeioMorto * monstrosPontos[1]) + (monstroHorrivelMorto * monstrosPontos[2])*0.10)
        print(f"o total de pontos mortos foram: {totalPontos}")
    if exercicios == 5:

        Numero1 = float(input("Insira o valor Numero1: "))##pega a nota inserido pelo usuário
        Numero2 = float(input("Insira o valor Numero2: "))##pega a nota inserido pelo usuário
        Numero3 = float(input("Insira o valor Numero3: "))##pega a nota inserido pelo usuário
        Numero4 = float(input("Insira o valor Numero4: "))##pega a nota inserido pelo usuário
        somaNumero = Numero1 + Numero2 + Numero3 + Numero4 
        print(somaNumero)

    if exercicios == 6:

        raio = float(input("Insira o valor da raio: "))
        area = (raio**2)/pi
        print(f"a area do circulo é: {area}")
    if exercicios == 7:
        nota1 = int(input("Insira a nota1: "))
        nota2 = int(input("Insira a nota2: "))
        nota3 = int(input("Insira a nota3: "))
        media = (nota1 + nota2 +nota3)/3
        print(f"a média da note é: {media}")

    if exercicios == 8:

        valor1 = float(input("Insira a valor1: "))
        valor2 = float(input("Insira a valor2: "))
        valor3 = float(input("Insira a valor3: "))
        mediaValor = (valor1 + valor2 +valor3)/3
        print(f"a média da note é: {mediaValor}")

    if exercicios == 9:
        valorPeso1 = float(input("Insira a valor1: "))
        valorPeso2 = float(input("Insira a valor2: "))
        valorPeso3 = float(input("Insira a valor3: "))  
        mediaPeso = valorPeso1 + (valorPeso2*2) + (valorPeso3*3)
        mediaTotal = mediaPeso/6
        print(f"A média total é: {mediaTotal}")
    if exercicios == 10:
        n1 = float(input("Insira n1: "))
        n2 = float(input("Insira n2: "))
        soma = n1 + n2
        diff = n1 - n2
        div = n1/n2
        prod = n1*n2

    
