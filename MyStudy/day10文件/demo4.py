#写入数据
''''
a: 追加方式-文件存在指针在末尾；文件不存在，创建新文件写入
w+: 读写 文件存在指针在末尾；文件不存在，创建新文件写入
'''
file=open("../bbb.txt",'a')
# con=file.read(10)
# print("写入前的数据：%s"%con)
file.write("cccb\nbbbb")
file.close()