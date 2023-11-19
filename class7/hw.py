# import random

# n = random.randint(1, 100)
# while True:
#     i = int(input("請輸入1到100的整數"))

#     if n < i:
#         print("在小一點") and print("請輸入i到n的整數")
#     elif n > i:
#         print("在大一點") and print("請輸入i到n的整數")
#     elif n == i:
#         print("恭喜猜中")
# break
import random

ans = random.randint(1, 100)
min = 0
max = 100
while True:
    x = int(input("請輸入" + str(min) + "~" + str(max) + "的整數"))
    if x == ans:
        print("恭喜猜中!")
        break
    elif x < ans:
        print("再大一點")
        if min < x < max:
            min = x
    elif x > ans:
        print("再小一點")
        if min < x < max:
            max = x
