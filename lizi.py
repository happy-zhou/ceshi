###例子：获取用户输入的个人信息，并且存储到字典中
# name=input("please input your name:")     #此时name是字符串变量
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
# studentlist=["dd","ds","gfg","efe","bgh","jk","kf"]    #数组
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
#自己写的
# r=list(range(1,31))
# g=list(range(1,36))
# y=list(range(1,4))
# a=list(range(1,6))
# for x in a:
#     for i in r:
#         print("距离红灯结束还有",31-i,"秒")    #print里的内容不是同一种数据类型要用逗号连接，同一数据类型可用加号连接
#     for j in g:
#         print("距离绿灯结束还有",36-j,"秒")
#     for k in y:
#         print("距离黄灯结束还有",4-k,"秒")

#老师写的
# light = {"红灯":30,"绿灯":35,"黄灯":3}    #用字典后期的可维护性更高，如果红绿灯的时间改变，只需要更改字典即可，而不需要更改循环
# while True:   #可以一直循环 ctrl+c退出死循环
#     for i in light:     #此时i遍历的是字典中的键，而非键对应的值
#         for j in range(light[i]):         #light[i]即取i键的值
#             print("距离",i,"结束还有",light[i]-j,"秒")

"""
实现一个注册的功能
用户输入账号密码，要求账号长度是5-8位，密码6-12位，并且账号须小写开头
存储到字典中{username:password}
"""

username =input("请输入账号：")
password =input("请输入密码：")
userinfo={username:password}
if  username !="":    #多层嵌套判断，也要保证if和else的结构对称
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
            if len(password)>=6 and len(password)<=12:
                print("注册成功！",username)
            else:
                print("密码长度要求6-12位")
        else:
            print("账号的首字母必须小写开头")
    else:
        print("账号长度要求5-8位")
else:
    print("账号不能为空！")

        












