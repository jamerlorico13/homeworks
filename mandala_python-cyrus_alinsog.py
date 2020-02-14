import turtle
turtle.bgcolor('black')
flow = turtle.Turtle()
flow.speed(100)
flow.color('purple')
for i in range(500):
    flow.forward(i)
    flow.left(100)

club = turtle.Turtle()
club.color('red')
club.speed(100)
for i in range(351):
    club.forward(i)
    club.left(152)

bc = turtle.Turtle()
bc.color('brown')
bc.speed(-1000)

for i in range(500):
    bc.forward(20)
    bc.right(6)
    bc.forward(4)
    bc.left(12)
    bc.forward(10)
    bc.right(6)

    bc.penup()
    bc.setposition(0, 0)
    bc.pendown()

    bc.right(1)
turtle.exitonclick()

#improvised from Michael0x2a code
