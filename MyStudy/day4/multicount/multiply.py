'''
计算从num1到num2的乘积
'''
def multiply_count(num1,num2):
    mul=1
    for num in range(num1,num2+1):
        mul*=num
        num+=1
    return mul
