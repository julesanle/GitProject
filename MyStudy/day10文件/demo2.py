#写入数据
''''
r: readonly-文件不存在，抛异常--文件指针在文件开头
r+ 读写 ；文件不存在，抛异常--件指针在文件开头
w: writable
'''
file=open("../aaa.txt",'r+')
# con=file.read()
# print("写入前：%s"%con)
file.write("dddddb\nbbbbb")
file.close()