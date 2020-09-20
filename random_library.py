import random
random.seed(10)  # 随机数种子，当随机数种子一样时，产生的随机数也一样，此随机数可复现
print(random.random())  # 当不使用随机数种子时，随机数默认是根据当前系统时间产生的，此随机数不可复现
random.seed(10)
print(random.random())  # random只能产生0到1之间的小数
print(random.random())

# random.randint(a,b) 生成一个[a,b]之间的随机整数
# random.randrange(m,n[,k]) 生成一个[m,n]之间以k为步长的随机整数
# random.getrandbits(k) 生成一个k比特长的随机整数
# random.uniform(a,b) 生成一个[a,b]之间的随机小数
# random.choice(seq) 从序列seq中随机选择一个元素，seq形式为[1,2,3,4,5,6,7]
# random.shuffle(seq) 将序列seq中的元素随机排列，返回打乱后的序列
