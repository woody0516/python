# import turtle

# turtle.penup()
# turtle.tracer(0, 0)

# for i in range(8):
#     turtle.right(45 * i)
#     turtle.forward(100)
#     turtle.stamp()
#     turtle.home()
# turtle.done()
import turtle
import time

turtle.pendown()
turtle.tracer(1, 0)  # 關閉動畫，參數說明：第一個參數代表每次更新畫面的時間間隔，第二個參數代表更新畫面的次數，0代表無限次

for i in range(60):
    turtle.right(i * 6)
    turtle.forward(100)
    turtle.home()
    time.sleep(1)
    turtle.clear()
