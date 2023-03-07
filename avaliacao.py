##importando a lib da tartaruga
import turtle as t
##criando a tartaruga
t.Turtle()
t.shape("turtle")
window = t.Screen()

repeticao = 0
while repeticao < 2:

    ## lista de cores

    color = ["Blue", "Red", "Yellow", "Black", "Purple", "Violet", "Green", "Cyan", "Orange", "White", "Salmon", "Pink", "Gray", "Brown", "Olive"]
    inputColor = t.textinput("Digite nome da cor ", "Em inglês")
    ## Seleção da lista de cores

    match inputColor:
        case "Blue":
            color = color[0]
        case "Red":
            color = color[1]
        case "Yellow":
            color = color[2]
        case "Black":
            color = color[3]
        case "Purple":
            color = color[4]
        case "Violet":
            color = color[5]
        case "Green":
            color = color[6]
        case "Cyan":
            color = color[7]
        case "Orange":
            color = color[8]
        case "White":
            color = color[9]
        case "Salmon":
            color = color[10]
        case "Pink":
            color = color[11]
        case "Gray":
            color = color[12]
        case "Brown":
            color = color[13]
        case "Olive":
            color = color[14]
        case _:
            t.write("Cor não encontrada, Tente novamente", align="left", font=('Arial', 15))
            t.ht()
            color = "White"

    if repeticao == 0:
        inputColor = color
        window.bgcolor(inputColor)

    if repeticao == 1:
        inputColor = color
        t.pencolor(inputColor)

    repeticao = repeticao + 1

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
t.done()
t.mainloop()
