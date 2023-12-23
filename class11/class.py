# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# food_list["果汁"] = 25
# food_list["冰淇淋"] = 10
# food_list["勒苟"] = 20

# items = food_list.items()
# for key, value in items:
#     if key == "果汁":
#         print(key + ": " + str(value) + "杯")
#     else:
#         print(key + ": " + str(value) + "分")
# # •
# # 在字典中新增「冰淇淋」10份。
# # •
# # 在字典中新增「熱狗」20份。
# # •
# # 修改字典中「果汁」的數量為25杯。
# parents_food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# print("還須購買的食物與數量")
# for key, value in items:
#     if key in parents_food_list:
#         if value > parents_food_list[key]:
#             print(key + ":" + str(value - parents_food_list[key]))
#     else:
#         print(key + ":" + str(value))
# food_list["蛋糕"] = 0
# food_list["三明治"] = 5
# food_list["果汁"] = 8
# food_list["薯條"] = 10
# food_list["披薩"] = 1
# food_list["冰淇淋"] = 3
# food_list["勒苟"] = 0

# delete_list = []

# for key, value in food_list.items():
#     if value == 0:
#         delete_list.append(key)

# for i in delete_list:
#     food_list.pop(i)
#     items = food_list.items()

# for key, value in items:
#     if key == "果汁":
#         print(key + ": " + str(value) + "杯")
# else:
#     print(key + ": " + str(value) + "分")


#  蛋糕：0份（已經吃完）
# •
# 三明治：5份
# •k

# 果汁：8杯
# •
# 薯條：10份
# •
# 披薩：1份
# •
# 冰淇淋：3份
# •
# 熱狗：0份（已經吃完）


#
gifts = {
    "小明": "樂高積木",
    "小花": "畫筆",
    "小強": "足球",
    "小美": "書",
    "小偉": "遙控車",
}
# 顯示一共收到了多少個禮物
print("一共收到了" + str(len(gifts)) + "個禮物")
for name, gift in gifts.items():
    print(name + "送了你一個" + gift)
