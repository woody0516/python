# sum = 0
# price = int(input("請輸入商品金額:"))
# while price != 0:
#     sum += price
#     print("目前總金額為" + str(sum) + "元")
#     price = int(input("請輸入商品金額:"))


# # import time

# # # # 輸入秒數
# # # second = int(input("請輸入秒數: "))
# # # # 倒數計時
# # # for i in range(second, 0, -1):
# # #     print(i)
# # #     time.sleep(0.00000000000001)
# # # else:
# # #     print("時間到!")


# # import time

# # # 輸入秒數
# # second = int(input("請輸入秒數: "))
# # # 倒數計時
# # while second > 0:
# #     print(second)
# #     time.sleep(0.00000000000001)
# #     second -= 1
# # else:
# #     print("時間到!")
# while True:
#     print("1. 蘋果汁")
#     print("2. 柳橙汁")
#     print("3. 葡萄汁")
#     print("4. 系統關閉")
#     ans = input("請輸入編號:")
#     if ans == "1":
#         print("您點的商品是蘋果汁")
#     elif ans == "2":
#         print("您點的商品是柳橙汁")
#     elif ans == "3":
#         print("您點的商品是葡萄汁")
#     elif ans == "4":
#         print("~~系統關閉~~")
#         break
#     else:
#         print("輸入錯誤查無此果汁，請重新輸入")
# 輸入要跳繩的次數
jump = int(input("請輸入要跳繩的次數："))
# 跳繩
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print("第" + str(i) + "次跳繩")
    # 練習:跳跳繩 # 輸入要跳繩的次數
jump = int(input("請輸入要跳繩的次數："))
# 跳繩
i = 1
while i <= jump:
    if i % 10 == 0:
        print("休息一下")
        i += 1
        continue
    print("第" + str(i) + "次跳繩")
    i += 1
