# import random
# print(random.randrange(3))
# randint函數
# import random

# # print(random.randint(1, 3))
# import random

# n = random.randint(1, 100)
# while True:
#     i = int(input("請輸入1到100的整數"))
#     if n < i:
#         print("在小一點")
#     elif n > i:
#         print("在大一點")
#     elif n == i:
#         print("恭喜猜中")
#         break
# l = [1, 2, 3, "hello", "world", [4, 5, 6]]
# print(l)
# i['a','b','c']
# i[0]
# i[1]
# 1[2]
# print(i[::3])

# l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(l[0])
# print(l[2])
# print(l[-1])
# print(l[-3])
# print(l[0:3])
# print(l[3:6])
# print(l[0:10:2])
# print(l[::2])
# print(len(l))
# for i in range(len(l)):
#     print(l[i])
# for i in l:
#     print(i)
juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]
while True:
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + juices_list[i])
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if ans == len(juices_list):
        print("~~系統關閉~~")
        break
    elif ans > len(juices_list) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print("您點的商品是" + juices_list[ans - 1])
