import turtle as t
##criando a tartaruga
t.Turtle()
t.shape("turtle")
import turtle
window = turtle.Screen()

##pegando informações do usuario 
bgcor = t.textinput("Digite nome da cor de fundo ","Em inglês")
window.bgcolor(bgcor)
pencor = t.textinput("Digite nome da cor de fundo ","Em inglês")

t.color('white')
t.pencolor(pencor)

## funções de movimento
def turn_left():
  t.left(20)

def turn_right():
  t.right(20)

def move_forward():
  t.fd(20)

def move_backward():
  t.fd(-20)

##leitor do teclado

window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")
window.onkeypress(move_forward, "Up")
window.onkeypress(move_backward, "Down")

window.listen()

turtle.done()
t.mainloop()