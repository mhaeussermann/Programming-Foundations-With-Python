import turtle as t

def draw_letters():
    window = t.Screen()
    window.bgcolor("white")

    pen = t.Turtle()
    pen.shape("turtle")
    pen.color("black")
    pen.speed(2)

    #Letter K
    pen.right(90)
    pen.forward(100)
    pen.home()
    pen.left(90)
    pen.forward(100)
    pen.home()
    pen.left(45)
    pen.forward(120)
    pen.home()
    pen.right(45)
    pen.forward(120)
    pen.penup()

    #Letter E without -
    pen.setpos(250,100)
    pen.right(135)
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(100)

    window.exitonclick()


draw_letters()
