from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(200)

def drawSquare(X):
    X.forward(200)
    X.left(90)
    X.forward(200)
    X.left(90)
    X.forward(200)
    X.left(90)


def drawTriangle(X):
    X.forward(120)
    X.left(90)
    X.forward(120)
    X.left(90)
    X.forward(120)
    X.left(90)
    

drawSquare(timmy)
timmy.penup()
timmy.backward(100)
timmy.pendown()
drawTriangle(timmy)          

newscreen = Screen()
print(newscreen.canvheight)
newscreen.exitonclick()