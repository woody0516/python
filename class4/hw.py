# """
# 測量你的BMI值, 確認你的體重是否正常?
# * BMI公式:體重(公斤) / 身高(公尺)的平方
# * BMI值正常範圍:14.8到20.7之間
# * BMI值過重範圍:20.7以上
# EX:
# 請輸入身高(公尺):1.7
# 請輸入體重(公斤):45
# 你的BMI為15.570934256055365
# 體重過輕
# 請輸入身高(公尺):1.7
# 請輸入體重(公斤):60
# 你的BMI為20.761245674740486
# 體重正常
# 請輸入身高(公尺):1.7
# 請輸入體重(公斤):90
# 你的BMI為31.14186851211073
# 體重過重
# """
hight = int(input("請輸入身高"))
Kilogram = int(input("請輸入體重"))
bmi = Kilogram / hight**2
if bmi >= 14.8 and bmi <= 20.7:
    print("體重正常")
elif bmi <= 14.7:
    print("體重過輕")
elif bmi >= 20.8:
    print("體重過重")
# """
# 輸入三角形三邊(存入變數a, b, c中)
# 判斷是否能構成三角形(利用邊長運算進行判斷，可以上網搜尋公式)
# 是三角形:則顯示面積和周長
# 不是:則顯示，無法構成三角形
# 三角形面積公式:
# p = 1/2 (a+b+c)
# area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# EX:
# a = 3
# b = 4
# c = 5
# 周長:12.0
# 面積:6.0
# a = 1
# b = 10
# c = 100
# 無法構成三角形
# """
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a + b > c and a + c > b and b + c > a:
    print(f"周:{(a+b+c)}")

    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"面積:{area}")
else:
    print("無法構成山腳型")
