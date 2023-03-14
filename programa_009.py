# Trabalhando com várias tartarugas
# Utilizando listas para controlar várias tartarugas
# programa_003.py

import turtle
import time
import random
import easygui

def finish_line():
    tartarugaf = turtle.Turtle()
    tartarugaf.fillcolor(cores[8])
    tartarugaf.shape("turtle")
    tartarugaf.color("Black")
    tartarugaf.penup()
    tartarugaf.speed(10)
    tartarugaf.setpos(600, -600)
    tartarugaf.pensize(10)
    tartarugaf.lt(90)
    tartarugaf.pendown()
    i = 0
    while i < 15:
        tartarugaf.pencolor("White")
        tartarugaf.fd(50)
        tartarugaf.pencolor("Grey")
        tartarugaf.fd(50)
        i = i+1


# Método para ir para frente
def move_frente(t, passos) -> None:
    t.fd(passos)
    return

if __name__ == "__main__":
    
    cores = ["Red", "Yellow", "Blue", "Orange", "Green", "Pink", "Purple", "Brown", "White"]
    random.seed(int(time.time()) )
    # Aqui pegamos os atributos gerais
    janela = turtle.Screen() # Vamos mexer em alguns atributos da tela
    janela.bgcolor('black') # Como mudar a cor do fundo

    turtle.penup()

    finish_line()

    qtd = easygui.integerbox("Entre com um número entre 1 e 8!", "Quantidade de tartarugas", 1,1,8)
    tartarugas = []
    y = -300
    for i in range(qtd):

        tartaruga = turtle.Turtle()
        tartaruga.penup()
        tartaruga.fillcolor(cores[i])
        tartaruga.shape("turtle")
        tartaruga.setpos(-700, y)
        y += 100
        tartarugas.append(tartaruga)
    turtle.pendown()



    vencedor = False
    while not vencedor:
        # Movendo cada tartaruga para a frente
        for tartaruga in tartarugas:
            move_frente(tartaruga, random.randrange(1, 11))
            if tartaruga.xcor() >= 600:
                vencedor = True
                color = tartaruga.fillcolor()+".png"
                msg = "Tartaruga " + tartaruga.fillcolor() + " venceu!!!"
                turtle.bgpic(color)
                easygui.msgbox(msg)
                break # quebra o for

    # Dizemos que se for pressionado q ou Q, a função fim deve ser chamada
    janela.onkeypress(exit, "q") 
    janela.onkeypress(exit, "Q") 
    janela.listen() 
    turtle.done() # Fica em espera
