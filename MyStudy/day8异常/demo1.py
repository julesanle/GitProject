def test():
    try:
        num=int(input("输入一个整数："))
        result=10/num
    except ValueError:
         print("值错误")
    except ZeroDivisionError:
        print("输入非0数字")
    except Exception as expresult:
        print(expresult)
    else:
        print("num:%s" % result)
        print("没有一点异常哦")
    finally:
        print("执行结束啦")

test()
