def multi_table():
    for line in range(1,10):
        for colum in range(1,line+1):
            print("%dx%d=%d"%(line,colum,line*colum),end='\t')
            colum+=1
        print()
        line+=1