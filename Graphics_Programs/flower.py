import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("green")

    for _ in range(36):
        pen.circle(100)
        pen.left(10)

    pen.right(90)
    pen.penup()
    pen.forward(200)
    pen.pendown()
    pen.left(90)

    pen.color("yellow")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()

    turtle.done()

draw_flower()