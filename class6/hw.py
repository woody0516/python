"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
word = int(input("請輸入一個數字"))
for i in range(1, word + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)

"""
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  * 
 *** 
*****
  * 
  * 
  * 
"""
n = int(input("請輸入要印出的箭頭大小"))
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (i * 2 + 1))

for i in range(n):
    print(" " * (n - 1) + "*")
