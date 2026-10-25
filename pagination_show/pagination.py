#造25 个学生编号(1~25)
student = [f"学生{i}" for i in range(1,26)]

page_size = 10  #每页10条

total = len(student)

pages = (total+page_size - 1) // page_size   #总页数

page = 1  #默认从第一页开始

while True:
    start = (page - 1) * page_size
    end = start + page_size
    print(f"---第 {page}/{pages} 页 ---")
    for stu in student[start:end]:
        print(" ",stu)

    if pages <= 1:
        break
    cmd = input("输入页码翻页(q 返回) : ").strip()
    if cmd.lower() == "q":
        break
    if cmd.isdigit() and 1 <= int(cmd) <= pages:
        page = int(cmd)
    else:
        print("页码无效,请从新输入！")


