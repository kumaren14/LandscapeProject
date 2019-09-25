import turtle

ian = turtle.Turtle()
alan = turtle.Turtle()
ellie = turtle.Turtle()
timmy = turtle.Turtle()

turtle.bgcolor("skyblue")

ian.speed(10)
alan.speed(10)
ellie.speed(10)
timmy.speed(10)

ian.shape("turtle")
alan.shape("turtle")
ellie.shape("turtle")
timmy.shape("turtle")

ian.penup()
alan.penup()
ellie.penup()
timmy.penup()

ian.goto(-500, -300)

ian.color("gray")
ian.pendown()

ian.begin_fill()
ian.left(55)
ian.forward(525)
ian.right(120)
ian.forward(400)
ian.left(145)
ian.forward(350)
ian.right(150)
ian.forward(350)
ian.left(110)
ian.forward(200)
ian.right(80)
ian.forward(200)
ian.goto(500, -300)
ian.goto(-500, -300)
ian.end_fill()
ian.penup()
ian.goto(-300, 300)
ian.left(45)

alan.color("forest green")



turtle.exitonclick()
