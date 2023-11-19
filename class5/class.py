# import turtle

# turtle.pensize(10)
# turtle.pencolor("yellow")
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(100)
#     turtle.right(145)

# turtle.end_fill()
# turtle.done()
# s = 0
# word = int(input("請用者輸入一個數字"))
# for i in range(word + 1):
#     s = s + i
# print(s)
# for i in range(1,10):
#     for j in range(1,10):
#         print(str(i)+"x"`+str(j)+"="+str(i*j))
# i=0
# while i<5:
#     print(i)
#     i=i+1
password = "hi"
while password != "1234":
    password + input("請輸入密碼:")
    if password == "1234":
        print("歡迎光鈴john")
    elif password == "5678":
        print("歡迎ray")
    else:
        print("密碼錯誤")
