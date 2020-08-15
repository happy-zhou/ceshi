import random

#产生10个随机数并放到列表中，
# list1=[]
# for i in range(10):
#     r=random.randint(1,100)
#     list1.append(r)    
# print(list1)

#产生10个不同的随机数放到列表中：
# list1=[]
# while len(list1)<10:
#     r=random.randint(1,30)
#     if r in list1:
#         continue
#     list1.append(r) 
# print(list1)

#找出列表中的最大值，不用max(list)
# list1=[]
# for i in range(10):
#     r=random.randint(1,100)
#     list1.append(r) 
# print(list1)
# mvalue=list1[0]
# for i in list1:       #for不仅可以实现整数的依次递增或者递减循环，还可以实现字符串、列表的遍历
#     if i>mvalue:
#         mvalue=i    
# print(mvalue)

#求和sum,排序sorted(),默认升序排序，sorted(list,reverse=True),此种情况是降序排序
# list1=[]
# for i in range(10):
#     r=random.randint(1,100)
#     list1.append(r) 
# print(list1)
# print(sum(list1))
# print(sorted(list1))

# s=[1,2,['nihao',4,2],5,2,[9,'s']]    #嵌套列表
# print(len(s))
# print(s[5][1])
# for i in  ****   #能够在for中循环的就是可迭代的(iterative),list()只能转换可迭代的数据类型


#对列表进行冒泡排序
# mylist=[3,8,1,0,7,2]
# for i in range(len(mylist)-1):
#     for j in range(len(mylist)-i-1):
#         if mylist[j]>mylist[j+1]:
#             mylist[j],mylist[j+1]=mylist[j+1],mylist[j]    #位置的互换
# print(mylist)


#字典的一些操作
# 案例：用户注册功能
# dic={}
# print('----------------欢迎来到直达售票系统---------------')
# username=input('请输入用户名:')
# passerword=input('请输入密码:')
# repassword=input('请确认密码：')
# phone=input('请输入电话号码：')
# if passerword==repassword:
#     dic['username']=username     #往空字典中添加元素
#     dic['password']=passerword
#     dic['phone']=phone
#     print('注册成功！')
#     print(dic)
# else:
#     print('两次密码不一致，请重新注册！')

# #字典的常用方法
# for i in dic.items():    #实现字典的遍历
#     print(i)    #此种方式键值对以元组的形式输出
# for key,value in dic.items():    #此种形式就可以实现取到key或者value
#     print(key)



#输出分数大于60分的同学名字
# chengji={}
# while True:
#     name=input('请输入学生姓名：')
#     score=int(input('请输入该学生分数：'))
#     chengji[name]=score
#     if name==' ':
#         break
# print(chengji)
# for name,score in chengji.items():
#     if score>60:
#         print(name)
#删除键值对，chengji.pop(),清除chengji.clear()


#集合，无序的不重复的元素序列
s1=set()   #集合的创建方式
#应用：一个列表快速去重
list1=[1,4,2,9,3,6,8,5,4]
print(set(list1))   #将列表相同的元素去除，并排序
s1.add('happy')    #添加一个元素
s1.add('day')
print(s1)