# print("你好，庆毅辉")   #只有字符串类型的需要加双引号或者单引号
# print(3+4)            #整数类型
# print("哈哈哈"*20)   #输出20个哈哈哈
# print(2>100)        #输出布尔值true或者false

#任何数据类型都可以转换成字符串str（除了空），int和float类型可以相互转换
# a = float(input("请输入a值："))   #数据类型的转换，如果不加float转换，a、b是字符串类型，输出结果会将两个值连接起来而不是相加
# b = float(input("请输入b值："))
# print(type(a))    #type表示输出数据类型
# print("输出:",a+b)

# a='sdfsdfgkvndfjsdmkvlfmvkdflvmskd'
# print(len(a))

#git和GitHub的关联在Python视频的第十五分钟左右

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
# b = [3,4,5,6,"xixi","haha",True,False,6,7,9,"庆毅辉"]  #数组用方括号
# b.append("大可爱")   #往数组尾巴追加一个元素
# print(b)
# b.insert(3,"你好呀")   #在数组下标为3的元素后面插入“你好呀”
# print(b)
# s=b.pop(0)  #剪切下标为0的元素
# z=b.pop(0)   #在上一步的基础上再剪切一次
# print(s+z)
# b.extend([2,3,9,"比心"])    #往数组尾巴上再扩充数组
# print(b)
# b.remove(5)    #在数组中删除元素为5的项
# print(b)

# """
# python的语法：
# 所有的函数都是小括号结尾
# 元组、数组、字典的取值，都是用[]
# 元组、数组、字典的定义：()[]{}
# """

# xx=[1,True,0,False]
# print(xx.count(0))     #False在程序运行时是当做0处理的



# """字典的特点
# 字典中值没有顺序
# 字典的接口必须是键值对的结构  键：值   key:value
# """
# a={"name":"zhangsan","gender":"nan","age":25}   #name、gender、age是key,相当于变量，后面跟的内容是value
# print(a["name"])   #取值，[]里面跟的是key
# a["weight"]="108斤"   #新增，在字典中新增内容
# print(a)
# a["name"]="xiaoming"   #修改name
# x=a.get("name")   #获取
# print(a)
# a.update(name="lisi")   #另一种实现新增或修改的方法update,可以同时更新多个
 del a["weight"]   #数组和字典的删除，[]里分别是主键和下标

###例子：获取用户输入的个人信息，并且存储到字典中
name=input("please input your name:")     #此时name是变量，不是字符串
age=input("please input your age:")
sex=input("please input your sex:")
a={"name":name,"age":age,"sex":sex}  
print(a)   



