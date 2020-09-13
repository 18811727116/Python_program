#String_Slice.py

string = "0123456789"
str1 = string[:10]
str2 = string[0:]
str3 = string[1:6:2]
str4 = string[::-1]
print(str1, str2, str3, str4)

print('这里有个双引号(")')
print("这里有个单引号(')")
print('''这里既有双引号(")又有单引号(')''')
print("这里有个双引号(\")")
print('这里有个单引号(\')')

s1 = "123"
s2 = "456"
s3 = s1 + s2 # 字符串拼接
s4 = 2 * s1
s5 = s2 * 2
print(s3, s4, s5)
print(len(s3))
print(str(100)) # str(x)将任意类型x转换成字符串形式，即给x加上引号
print(eval(s3)) # eval(x)将x的外侧引号去掉，str函数和eval函数是一对
print(hex(eval(s3))) # hex(x)整数x的十六进制表示
print(oct(eval(s3))) # oct(x)整数x的八进制表示
print("我爱中国" + s1)

s6 = "AbCdEfGh"
print(s6.lower())
print(s6.upper())
s7 = "A,B,C"
print(s7.split(",")) # 返回一个列表，由,分隔的部分组成
s8 = "hello wudan, wudan love China"
print(s8.count("wudan")) # str.count(sub) 返回子串sub在str中出现的次数
print(s6.replace("h", "WUDAN")) # str.replace(old, new)返回字符串str副本，所有old子串被替换成new新串
print("python".center(20, "=")) # str.center(width[,fillchar]),字符串str根据宽度width居中，fillchar可选
print("= python = ".strip(" =np")) # str.strip(chars)，从str中去掉在其左侧和右侧chars中列出的字符
print("wudan".join("12345")) # str.join(iter) 在iter变量除最后元素外每个元素后面增加一个str

#当print中没有end操作时，默认有换行符的（即两个print输出有换行符，上面例子可以看出），当有end操作时就改变了默认输出规则，根据自己修改的规则输出
for i in range(5):
    print(i, end="") # 连着输出
for i in range(5):
    print(i, end=" ") # 空格输出
for i in range(5):
    print(i, end="\n") # 换行输出

# format()格式控制输出
print("{0:=<20}".format("python"))
print("{0:=^20}".format("python"))
print("{0:=>20}".format("python"))
print("{0:,.2f}".format(12345.6789)) # 加上千位分隔符
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
