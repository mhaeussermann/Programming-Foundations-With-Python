import turtle as t

def draw_square():
    window = t.Screen()
    window.bgcolor("red")

    hedgehog = t.Turtle()

    iteration = 0
    while iteration < 4:
        hedgehog.forward(100)
        hedgehog.right(90)
        iteration +=1

    window.exitonclick()

draw_square()
