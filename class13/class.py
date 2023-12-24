# inp=eval(input("請輸入一個算是"))
# print(inp)
# import os

# file_path = "C:/Users/user/Desktop/python/class11/class.py"
# if os.path.isfile(file_path):
#     print("檔案純在")
# else:
#     print("檔案不純在")
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close
path='C:\Users\user\Desktop\python\class13\class.py'
f=open(path,'r')
total=f.read()
print(total)
f.close()

path='C:\Users\user\Desktop\python\class13\class.py'
f=open(path,'r')
lines=f.readlines()
for line in lines:
    print (line)
f.close()