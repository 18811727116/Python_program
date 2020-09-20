import turtle


def koah(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koah(size/3, n-1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koah(400, level)
    turtle.right(120)
    koah(400, level)
    turtle.right(120)
    koah(400, level)
    turtle.hideturtle()
    turtle.done()


main()
