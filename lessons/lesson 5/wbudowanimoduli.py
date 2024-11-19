import turtle


def drow_squar(size, color):
    turtle.speed(3)
    turtle.color(color)
    turtle.begin_fill()
    def move(len):
        turtle.forward(len)
        turtle.left(90)

    for _ in range(4):
        move(size)

    turtle.end_fill()

drow_squar(100, "red")
turtle.goto(20, 20)
drow_squar(200, "blue")
