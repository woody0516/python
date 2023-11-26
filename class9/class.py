# 重組字串
# img=['1','2','3']
# '-'.join(img)
# img = "2023/10/23".split("/")
# print("-".join(img))
# "1,2,3,".split(",")
# l=[1,2,3]
# l.insert(0,'a')
# print(l)

order_list = []
while True:
    print("歡迎使用點摻機!")
    print("1.新增餐點到點餐清單")
    print("2.從點餐清單中移除特定餐點")
    print("3.在指定位置加入餐點")
    print("4.計算點餐清單中某餐點的數量")
    print("5.取消點餐清單中的最後一項餐點")
    print("6. 取消點餐清單中特定位置的餐點")
    print("7.顯示升序排序的點餐清單")
    print("8. 查詢餐點在點餐清單中的")
    print("9.反轉點餐清單的順序")
    print("10.查詢餐點在點餐清單中的位置")
    print("11. 離開點餐機")

    option = input("歡迎使用點餐機!情選擇尼想要用的功能:")

    if option == "1":
        l = input("請輸入您想要新增的餐點:")
        order_list.append(l)
    elif option == "2":
        l = input("請輸入您想要移除的餐點:")
        if l in order_list:
            order_list.remove(l)
    elif option == "3":
        l = int(input("請輸入您想要在指定位置:"))
        j = input("請輸入您想要加入的餐點:")
        order_list.insert(l, j)
    elif option == "11":
        print("謝謝使用點餐機")
        break
    else:
        print("請輸入有效的選擇")
        continue
    print("目前的點餐清單:" + str(order_list))
# l=[1,2,3]
# l.append(4)
# print(l)
