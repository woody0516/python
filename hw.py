# """
# 以下功能說明:
# 1. 新增餐點
#     1.1 顯示餐點列表
#     1.2 輸入餐點編號
#     1.3 將餐點加入my_list
# 2. 移除餐點
#     2.1 輸入想移除的餐點完整名稱
#     2.2 將餐點從my_list移除
# 3. 提交菜單
#     3.1 顯示my_list中的餐點及數量
#     3.2 顯示"菜單已提交囉!"
# """
order_list = []
menu = ["apple", "banana", "lemon"]
while True:
    print("1.新增餐點")
    print("2.移除餐點")
    print("3.提交菜單")

    option = input("歡迎使用點餐機!請選擇你想要用的功能:")
    if option == "1":
        l = input("請輸入您想要新增的餐點:")
        order_list.append(l)
    elif option == "2":
        l = input("請輸入您想要移除的餐點:")
        while l in order_list:
            order_list.remove(l)
    elif option == "3":
        print(order_list.count(menu[0]))
        break
    else:
        print("請輸入有效的選擇")
        continue
    print("目前的點餐清單:" + str(order_list))
