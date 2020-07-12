###例子：获取用户输入的个人信息，并且存储到字典中
# name=input("please input your name:")     #此时name是变量，不是字符串
# age=input("please input your age:")
# sex=input("please input your sex:")
# a={"name":name,"age":age,"sex":sex}  
# print(a)



"""
现在有10个学生的成绩需要录入到系统中，人物分别是1，2，3.......
名字和成绩必须对应上，大于60和小于60的分开存放
"""
#while循环
# highscore={}
# lowscore={}
# studentlist=["dd","ds","gfg","efe","bgh","jk","kf"]
# a=0
# while a<len(studentlist):
#     chengji=input("请输入"+studentlist[a]+"的成绩：")
#     chengji=int(chengji)
#     if chengji>60:
#         highscore[studentlist[a]]=chengji    #将学生成绩存到字典中
#     else: 
#         lowscore[studentlist[a]]=chengji 
#     a=a+1     #控制下标的变化来循环实现学生姓名的切换
# print("成绩大于60分的：",highscore) 
# print("成绩小于60分的:",lowscore)

#for循环
# highscore={}
# lowscore={}
# studentlist=["dd","ds","gfg","efe","bgh","jk","kf"]
# for i in studentlist:
#     chengji=input("请输入"+i+"的成绩:")
#     chengji=int(chengji)
#     if chengji > 60:      #后面的冒号一定不能忘,python中缩进很重要，缩进相同字符的为一模块
#         highscore[i]=chengji
#     else:
#         lowscore[i]=chengji
#         print(highscore)
#         print(lowscore)


#练习输出99乘法表
# for i in range(1,10): 
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="  ")   #end=""控制不换行
#     print()    #此处是为了一次for循环之后切换到下一行


#通过print打印，模拟一个红绿灯的功能；红灯30次后绿灯35次再黄灯三次，循环5次
r=list(range(1,31))




"""
实现一个注册的功能
用户输入账号密码，要求账号长度是5-8位，密码6-12位，并且账号须小写开头
存储到字典中{username:password}
"""









