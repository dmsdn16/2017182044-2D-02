import turtle as t
t.penup()
t.goto(-250,250)
t.pendown()
for i in range(6):
    t.forward(500)
    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(500)
    t.right(180)
    t.pendown()


t.left(90)
t.penup()
t.forward(100)
t.pendown()
for i in range(6):
    t.forward(500)
    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(500)
    t.right(180)
    t.pendown()


t.exitonclick()
