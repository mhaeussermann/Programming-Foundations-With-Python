import turtle as t

def draw_square(some_t):
    iteration = 0
    while iteration < 4:
        some_t.forward(100)
        some_t.right(90)
        iteration +=1

def draw_art():
    window = t.Screen()
    window.bgcolor("blue")

    #Square
    hedgehog = t.Turtle()
    hedgehog.shape("turtle")
    hedgehog.color("white")
    hedgehog.speed(2)

    iteration = 0
    while iteration < 36:
        draw_square(hedgehog)
        hedgehog.right(10)
        iteration += 1
    
    #Circle
    #eagle = t.Turtle()
    #eagle.shape("arrow")
    #eagle.color("grey")
    #eagle.circle(100)

    #Triangle
    #lizard = t.Turtle()
    #lizard.shape("triangle")
    #lizard.color("black")
    #steps = 0
    #while steps < 3:
        #lizard.forward(175)
        #lizard.left(120)
        #steps += 1

    window.exitonclick()

draw_art()
