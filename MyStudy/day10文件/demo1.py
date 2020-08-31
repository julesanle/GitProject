file=open("../center_list.txt")
con=file.read(10)
print("第一次读取后指针位置：%s"%file.tell())
print(con)

#指针重置
file.seek(0)
print("重置后指针位置：%s"%file.tell())
# con=file.read()
conn=file.read(10)
print(conn)
file.close()

#二进制文件
file2=open("../picture.jpg",'rb')
con2=file2.read()
print(con2)
file2.close()

