#判断的三种形式：if；if else;if elif else;
# a=3
# b=9   #在python中以首字母对齐为一个代码块
# if a==b:       #一层if
#     print("hahahaha")


# if a>b:         #两层if
#     print(a)    #if形式正确，print会自动缩进四个字符
# else:
#     print(b)


# age=int(input("请输入你的年龄："))   #用input的时候，是字符串类型，所以要加int进行数据类型转换
# if age >60:   #多层if
#     print("你该退休啦")
# elif age>30:
#     print("你该好好工作啊")
# elif age>20:
#     print("你应该好好规划你的职业")
# else:
#     print("你该好好读书")

#in判断是否具有包含关系，对立的就是not in
# a=("你好")
# if a in "你好，吃饭了嘛":    #a是否包含于in后面的表达式
#     print("哈哈哈")

# a = input(" please input a:")
# if a=="":                       #判断输入的内容是否为空
#     print("输入的内容不能为空!")
#     exit()              #exit()可以直接退出
# if  a in "012345678":
#     a=int(a)         #将输入的字符串类型转换成整数类型，进行下面的判断
# else:
#     print("请输入正确的内容!")
#     exit()
# if a<3:
#     print("婴儿")
# else:
#     print("儿童")


#is一般用来判断数据类型,对立的就是not is
# a=100
# if type(a) is int:
#     print("zhengshu")
# elif type(a) is str:
#     print("zifuchuan")
# else:
#     print("qitaleixing")

#循环
"""
现在有10个学生的成绩需要录入到系统中，人物分别是1，2，3.......
名字和成绩必须对应上，大于60和小于60的分开存放
"""
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
#实现遍历
studentlist=["dd","ds","gfg","efe","bgh","jk","kf"]
for i in studentlist:    #i表示遍历对象里的每一个值
    print(i)

b=list(range(0,100))   #range表示生成一个数列，list将这个数列转换成数组，此时默认步长/步进为1
q=list(range(1,100,2))   #此时表示步长为2,b步长还可以为负数
