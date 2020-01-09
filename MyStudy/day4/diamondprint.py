'''
打印菱形
    *
  * * *
* * * * *
  * * *
    *
'''
endnum=int(input("请输入打印的行数，必须为奇数："))
for line in range(0,endnum):
    for colum in range(0,endnum):
        if line<=endnum//2:
            if colum>=endnum//2-line and colum<=endnum//2+line:
                print("*",end=' ')
            else:
                print(' ', end=' ')
        else:
            if colum>=line-endnum//2 and colum<int(1.5*endnum-line):
                print("*",end=' ')
            else:
                print(' ', end=' ')
        colum+=1
    print()
    line+=1


