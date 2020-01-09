start=int(input("请输入起始数字："))
end=int(input("请输入结束数字："))
print("%d到%d的质数有："%(start,end))
for i in range(start,end+1):
    if i==2 or i==3:
        print(i,end=" ")
    else:
        for j in range(2,i//2+1):
            if i%j==0:
                j += 1
                break
            j+=1
            if j==i//2+1:
               print(i,end=" ")
    i+=1


