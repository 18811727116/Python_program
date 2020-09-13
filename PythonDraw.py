PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200) # 设置一个窗体
turtle.penup()
turtle.fd(-250) # 海龟前进方向
turtle.pendown()
turtle.pensize(50)
turtle.pencolor("gold")
turtle.seth(-40) # 海龟方向
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()


# import turtle
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# #turtle.left(45)
# turtle.seth(45)
# turtle.fd(100)
# turtle.done()

