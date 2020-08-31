#写入数据
''''
w: writable-文件存在会覆盖；文件不存在，创建新文件
w+: 读写 --文件存在会覆盖；文件不存在，创建新文件
'''
file=open("../bbb.txt",'w+')
con=file.read(10)
print(con)
# file.write("bbbb\nbbbb")
# file.close()