def exit():
    print("提交,平均分數為:" + str(sum(grade.values()) / len(grade)))


def add():
    subject = input("請輸入想新增的科目:")
    score = eval(input("請輸入分數:"))
    grade[subject] = score


def delete():
    subject = input("請輸入想刪除的科目:")
    # try:
    #     grade.pop(subject)
    # except:
    #     print("此科目不存在")

    grade.pop(subject, None)

    # if subject in grade:
    #     grade.pop(subject)
    # else:
    #     print("此科目不存在")


grade = {}
option = [add, delete, exit]
while True:
    for subject, score in grade.items():
        print(subject + ":" + str(score))
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    try:
        select = int(input("請輸入功能編號"))

    except:
        print("輸入錯誤，請重新輸入")
    else:
        if select > len(option) or select < 1:
            print("輸入錯誤，請重新輸入")
        elif select == len(option):
            exit()
            break
        else:
            option[select - 1]()
