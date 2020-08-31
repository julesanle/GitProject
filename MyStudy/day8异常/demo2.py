def input_password():
    password = input("请输入密码：")
    if len(password) >= 8:
        return password
    print("主动抛出异常")
    exception1 = Exception("密码长度不够")
    raise exception1

try:
    print("密码是：%s" % input_password())
except Exception as result:
    print(result)



