file=open("../center_list.txt")
while True:
    # 读取一行
    con=file.readline()
    print("读取后指针位置：%s"%file.tell())
    if not con:
        break
    print(con)
file.close()