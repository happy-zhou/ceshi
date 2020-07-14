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
def jiafa(a,b):
    """
    这个方法的作用是实现两个数字相加      #对函数进行注释，将鼠标放在函数名上就会显示该注释
    """
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "输入的数据类型不正确"
jiafa(1,67)
#用return返回，返回后我们可以对这个值做其他操作，而print不能
a=jiafa(3,4)
print(a+1)    #而如果前面用的print,则不能对a做其他操作


#异常捕获，一般用来判断用户的输入，代码报错就是异常
try:
    print("a"+1)
except:
    print("上面的代码写错了")     #try和except是成对出现的，先运行try,try为true则不会执行except


#包、模块、类、方法、变量  包含又并列的关系
#pip install pymysql  安装数据库的包





