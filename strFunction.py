import random


#使用while循环实现输出1-50之间的偶数和
# sum=0
# i=1
# while i<=50:
#     if i%2==0:
#         sum=sum+i
        
#     i=i+1
    
# print(sum)


#字符串的格式化与逆序
# name='tomnjsdbjdsncjcvsdjncsjdcnjd'
# print(' %s说：大家好好学习'%name)   
# print(len(name))
# print(name[0:28])  #字符串的正序取值，默认步长为1
# print(name[28:0:-1])   #字符串的逆序，-1表示取值的方向从右往左
# print(name[::-1])     #字符串逆序的常用写法
# print(name[0:28:2])   #正序取值，步长为2

# str='hello word'
# print(len(str))
# print(str.index(' '))
# print(str[len(str):str.index(' '):-1])  #将Word逆序
# print(str[::-1])   #str字符串逆序

# #字符串的内置函数之大小写
# print(str.capitalize())    #调用函数capitalize,第一个字母大写
# print(str.title())   #title函数，每个单词的首字母大写
# print(str.istitle())   #判断字符串的每个单词是否大写，返回类型为布尔值
# print(str.upper())    #将所有字母全部转换成大写
# print(str.lower())     #将字符串中的大写字母转换成小写
# #验证码案例
# s='QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890'
# code=''
# for i in range(4):
#     ran1=random.randint(0,len(s)-1)
#     code=code+s[ran1]
# print(code)
# code1=code.lower()
# user_input=input('请输入验证码：')
# if user_input==code or user_input==code1:     #用户在输入大写或小写的时候都正确，所以要有一个转换
#     print('通过验证')
# else:
#     print('验证码错误，请重新输入！')


#字符串内置方法之查找和替换
s='ahmd chd even93 DaVFYmj'
# print(s[3:])   #下标从3开始的所有字符
# print('F' in s)   #返回值为布尔值
# p1=s.find('h')     #find函数如果能找到则返回下标志，下标是字母第一次出现的位置，不能找到就返回-1，index和find的区别是index找不到会报异常
# print(s.find('h'))    #print输出类型为字符串型
# p2=print(s.find('h',p1+1,len(s)-1))   #找第二个h出现的位置，查找范围是[p1+1,len(s)-1],末端位置可以省略()
# p3=print(s.rfind('m'))   #从右侧开始找，lfind同理，从左边开始找,rindex和lindex同理
# s1=print(s.replace(' ','#'))   #replace(before,after),用#替换空格；也可以用替换删除空格，replace(' ','')


#字符串内建函数encode()，decode()
# st='希望大家都能拥有一个好心情'
# print(st.encode('utf-8'))   #在网络中传输要编码，编码类型不指定就默认utf-8，还有gbk.......
# ab=st.encode('utf-8')
# print(ab.decode('utf-8'))    #注意使用decode必须编码之后的字符串，而不能对st解码

#判断开头结尾startwith（）和endwith()，返回的是布尔值，一般用于上传文件判断格式；
#str.isalpha()判断str是否是字母，isdigit()是否是数字
# filename='happy,txt'
# print(filename.endswith('doc'))
# print(filename.startswith('h'))

# #合并、拆分
# name=['zhangsan','happy','zhoujuan','wangwu']    #[]表示列表
# result='-'.join(name)  #将列表中的字符串用空格连接起来
# print(result)
# print(max(name))   #max()和min()也可以用来比较字母的大小
# b=s.split(' ')   #以空格为分隔符，将分割后的字符放到一个列表中
# print(b)


#作业1：输入两个字符串，从第一个字符串中删掉第二个字符串中的所有字符，输出第一个结果字符串
# s1=input('请输入第一个字符串：')
# s2=input('请输入第二个字符串：')
# s3=''
# for i in s1:
#     # if i in s2:
#     #     s1=s1.replace('','i')
#     if i not in s2:
#         s3=s3+i
# print(s3)
# for i in s2:      #第二种方法
#     s1=s1.replace(i,'')
# print(s1)


#作业2：小易喜欢的单词具有以下特性：每个字母都是大写字母，单词没有连续相等的字母；随意给一个单词，判断小易是否喜欢这个单词
# word=input('请输入单词：')
# if word.isupper() is True:
#     for i in range(0,len(word)-1):
#         if word[i]==word[i+1]:
#             print('小易不喜欢，是叠词！')
#     else:                            #for和else也可以成对出现
#          print('小易喜欢这个单词')    
# else:
#     print('不是大写，小易不喜欢！')



#作业3：循环提示用户输入：用户名、密码、邮箱（要求用户输入的长度不超过20个字符，如果超过则只有前20个有效），如果用户输入q或者Q则表示停止输入
s=''
while True:
    name=input('请输入用户名：')
    if len(name)>20:
        name=name[0:20]
    password=input('请输入密码：')
    mail=input('请输入邮箱：')
    dit='{}\t{}\t{}\n'.format(name,password,mail)       #\t表示空格，\n表示换行,format是格式化的一种形式
    s=s+dit
    if name=='q' or name=='Q':
        break
print(s)
    
