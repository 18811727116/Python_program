# 使用try和except来异常处理，程序如果正确运行就只会运行try里面的语句，如果发生错误，则会运行except里面的语句
try:
    num = eval(input("请输入一个整数: "))
    print(num**2)
except NameError:
    print("输入不是整数")
'''
# 异常处理的高级使用
try:
    语句块1
except NameError:     # 发生异常时执行
    语句块二
else:       # 不发生异常时执行，即在执行try语句块后执行
    语句块三
finally:    # 不管发生异常与否，都要执行
    语句块四
'''