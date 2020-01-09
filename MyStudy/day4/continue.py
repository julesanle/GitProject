# 写一个报数的小功能，遇到4跳过报下一个数
start=1
jumpnum=input("请输入跳过时数字需要包含的数：")
endnum=int(input("请输入最大数字："))
while(start<endnum):
    if str(start).__contains__(jumpnum):
        start+=1
        continue
    print(start,end=' ')
    start+=1
