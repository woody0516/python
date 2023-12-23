grade = {}
while True:
    for subject, score in grade.items():
        print(subject + ":" + str(score))
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    select = input("請輸入功能編號:")
    if select == "1":
        subject = input("請輸入想新增的科目:")
        score = eval(input("請輸入分數:"))
        grade[subject] = score

    elif select == "2":
        subject = input("請輸入想新增的科目:")
        # try:
        #     grade.pop(subject)
        # except:
        #     print("此科目不存在")

        grade.pop(subject, None)

        # if subject in grade:
        #     grade.pop(subject)
        # else:
        #     print("此科目不存在")

    elif select == "3":
        print("提交,平均分數為:" + str(sum(grade.values()) / len(grade)))
        break
    else:
        print("查無此功能請重新輸入")
