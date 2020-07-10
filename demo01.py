# print("你好，庆毅辉")   #只有字符串类型的需要加双引号或者单引号
# print(3+4)
# print("哈哈哈"*20)   #输出20个哈哈哈
# print(2>100)

# a = float(input("请输入a值："))   #数据类型的转换，如果不加float转换，a、b是字符串类型，输出结果会将两个值连接起来而不是相加
# b = float(input("请输入b值："))
# print("输出:",a+b)

# a='sdfsdfgkvndfjsdmkvlfmvkdflvmskd'
# print(len(a))

# a=input("请输入字符串1:")     #读入两个字符串，并计算字符串长度之和
# b=input("请输入字符串2：")
# print(len(a)+len(b))

# 元组，下标，从0开始标
#a=(3,4,5,6,"xixi","haha",True,False,6,7,9,"庆毅辉")   #元组可以有多种数据类型混合
# print(a)
# print(a[4])  #输出元组中为下标为4的的内容
#print(a[-1])  #下标也可以倒着数（从右往左），为负数
# print(a.index("庆毅辉"))   #返回庆毅辉的下标
# print(a.count(6))   #返回6出现的次数
#切片
# print(a[0:4])  #有左闭右开原则，取下标为0，1，2，3的这四个元素
# print(a[3:])  #取a中下标从3开始的所有元素
# print(a[:7])    #取a中下标从0到6 的所有元素

# 二维元组(元组里面又嵌套元组)
# a=(3,4,5,6,"xixi","haha",True,False,6,7,9,"庆毅辉")  #元组用圆括号
# d=(a,45,6,2,89,True)
# print(d[0][11])    #a在d中的下标是0，庆毅辉在a中的下标是11
# print(d.count(2))

#元组一旦输入之后不可修改，但是数组可以修改
b = [3,4,5,6,"xixi","haha",True,False,6,7,9,"庆毅辉"]  #数组用方括号
b.append("大可爱")   #往数组尾巴追加内容
print(b.append)
