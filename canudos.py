import turtle as t

t.Turtle()
t.shape("turtle")

inicial = t.pos()
import turtle
window = turtle.Screen()
window.bgcolor('black')
t.color('white')

bullet = turtle.Turtle()
bullet.shape("circle")
bullet.hideturtle()
bullet.shapesize(0.3)
bullet.color("red")
bullet.speed(1)
bullet.penup()
t.penup()

"""
def shoot():
    bullet.hideturtle()
    bullet.showturtle()
    bullet.fd(300)
    bullet.clear()
    bullet.hideturtle()
"""

def turn_left():
  t.left(20)
  bullet.left(20)

def turn_right():
  t.right(20)
  bullet.right(20)

def move_forward():
  t.fd(20)

def move_backward():
  t.fd(-20)

    
window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")
window.onkeypress(move_forward, "Up")
window.onkeypress(move_backward, "Down")
window.onkeypress(shoot, "a")



window.listen()

turtle.done()

"""
#quadrado
t.color("red")
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)



#escada

t.penup()
t.hideturtle()
t.setpos(inicial)
t.showturtle()
t.pendown()

t.rt(90)
t.fd(100)
t.rt(125)
t.fd(200)
t.rt(110)
t.fd(200)
t.rt(125)
t.setpos(inicial)

"""
t.mainloop()
