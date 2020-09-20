# 利用递归绘制科赫雪花
import turtle


def koah(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koah(size/3, n-1)


def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koah(600, 3)  # 三阶科赫曲线，3是阶数
    turtle.hideturtle()
    turtle.done()


main()