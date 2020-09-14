#方法/函数的定义
#自动判断账号长度是八位，并且账号必须小写开头
# def check(username):
#     if  username !="":    #多层嵌套判断，也要保证if和else的结构对称
#         if len(username)>=5 and len(username)<=8:
#             if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
#                 print("ok")
#             else:
#                 print("账号的首字母必须小写开头")
#         else:
#              print("账号长度要求5-8位")
#     else:
#          print("账号不能为空！")
# check("21324")

"""
def 方法的声明
check 方法的名字
username  方法里的参数/变量
引号后面的内容是方法的逻辑代码
"""
# def jiafa(a,b):
#     """
#     这个方法的作用是实现两个数字相加      #对函数进行注释，将鼠标放在函数名上就会显示该注释
#     """
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return "输入的数据类型不正确"
# jiafa(1,67)
# #用return返回，返回后我们可以对这个值做其他操作，而print不能
# a=jiafa(3,4)
# print(a+1)    #而如果函数里面用的print,则不能对a做其他操作


# #异常捕获，一般用来判断用户的输入，代码报错就是异常
# try:
#     print("a"+1)     #字符串型和整数型无法运算
# except:
#     print("上面的代码写错了")     #try和except是成对出现的，先运行try,try为true则不会执行except
# finally:          #无论有没有错误都会执行的部分
#      pass
# #异常类d 
# try:
#     print(jkdb+1)
# except Exception as err:                #Exception是异常类，err包含了异常的原因
#     pass:
#     print("上面的代码写错了") 

"""
包、模块、类、方法、变量  包含（如方法里面包含了变量）又并列（如jiafa(a,b)中方法和变量同时出现）的关系
包有系统自带的包和第三方的包,第三方的包需要安装
import time  #导入自带time包，一般写到py文件的最上方
time.sleep(1)    #停顿一秒

pip install pymysql  #安装第三方数据库的包,会自动下载
pip list   #显示所有第三方的包
pip uninstall bao     #删除第三方的包
"""    

"""
ctrl+/多行快速注释
class 声明类的名字     #类名字的首字母必须大写
面向对象编程
类里面所有的方法都必须要传一个参数，叫self,指类自己
"""
class  Girlfriend():
    # def __init__(self):       #相当于初始化,内在属性已经确定
    #     self.sex="女"
    #     self.height="165"
    #     self.weight="55kg"
    #     self.hair="黑长直"
    #     self.age="24"

    def __init__(self,sex,height,weight,hair,age):       #这样定义所有的属性可以自己随意输入
        self.sex=sex
        self.height=height
        self.weight=weight
        self.hair=hair
        self.age=age

    def caiyi(self,num):     #方法里面的第一个参数必须是self
        if num==1:
            print("精通八大菜系")
        elif num==2:
            print("唱歌跳舞打篮球")
        else:
            print("安安静静的读书")

    def work(self):
        print("程序员")

#类的实例化
#manyiyi=Girlfriend()    #针对第一种init,前面只是声明和定义了类，现在赋值给具体的对象manyiyi
#manyiyi=Girlfriend("女","165cm","55kg","黑长直","24")
#manyiyi.work()    #只有self参数的方法调用时参数可以为空   
#manyiyi.caiyi(1)
#print(manyiyi.sex)


#类的继承
# class Nvpengyou(Girlfriend):    #Nvpengyou子类继承了Girlfriend父类的所有方法和属性
#     def xingge(self):
#         print("乐观外向，善解人意")    #在子类中也可以定义新的方法
# liuyifei=Nvpengyou("女","165cm","55kg","黑长直","24")
# liuyifei.caiyi(6)
# liuyifei.xingge()


#文件的读写
text=input("请输入今天的心情：")
with open("日记.txt","a",encoding="utf8")  as f:    #w表示写入，原来的会清空，a表示追加，utf8是文件的编码规则
    f.write(text+"\n")   #\n表示自动换行，\t表示空格


with open("D:\workhome\github\ceshi\日记.txt","r") as f:
    f.read(text)    #读文件



#对象----具体的事物，世间万物皆对象



