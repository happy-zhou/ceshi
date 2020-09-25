
from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque
import turtle
#栈的操作
# s=Stack() 
# print(s.isEmpty())
# s.push(4)
# s.push('cat')
# print(s.peek())   #从栈返回顶部项
# s.push('hello')
# s.pop()     #出栈
# s.size()

#例子：十进制转换成二进制，采用的是“除以2求余数法”，每次得到的余数就是由低到高的二进制位,所以需要一个栈来进行次序反转
#十进制转换成N进制，只要将除以2求余数改成除以N求余数就可以
# def divideby2(decnumber):
#     remstack=Stack()
#     while decnumber>0:
#         rem = decnumber % 2   #求余
#         remstack.push(rem)
#         decnumber=decnumber//2   #整数除

#     binstring=''
#     while not remstack.isempty():
#         binstring=binstring+str(remstack.pop())
#         return binstring
# print(divideby2(56))


#队列的操作以及例子
#热土豆（约瑟夫问题），传烫手的热土豆，喊停的时候热土豆在谁的手里谁就出局,输出最后留下的人
# def hotPotato(namelist,num):
#     simqueue=Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#         while simqueue.size()>1:
#             for i in range(num):
#                 simqueue.dequeue()
#                 simqueue.enqueue()
#             simqueue.dequeue()
#         return simqueue.dequeue()
# print(hotPotato(['sas','ffv','njvf','njk','vf','eur','jio','pou','bx'],5))  #土豆原本在第一个人手上，喊5停的时候应该在第六个个人手上

#双端队列应用：回文词的判定
# d=Deque()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(6)
# print(d.size())
# print(d)
# d.removeRear()
# d.removeFront()
# 应用：回文词的判定
# def palchecker(str1):
#     chardeque=Deque()
#     for ch in str1:
#         chardeque.addRear(ch)
#     stillEqual=True
#     while chardeque.size()>1 and stillEqual:
#         first=chardeque.removeFront()
#         last=chardeque.removeRear()
#         if first != last:
#             stillEqual = False
#     return stillEqual
# print(palchecker('abcddcba'))
# print(palchecker('msjfddkdsm')

#递归：将问题分解为规模更小的相同问题，直到问题小到可以用非常简单直接的方式解决；规模在逐渐向基本结束条件演进；在方法中调用自身
#递归数列求和：数列的和=首个数+余下数列的和
# def listsum(numlist):
#     if len(numlist)==1:
#         sum=numlist[0]
#     else:
#         return numlist[0]+listsum(numlist[1:])    #相当于numlist又是一个新的列表
# print(listsum([1,3,5,7,9]))
#任意进制的转换：
def toStr(n,base):    #整数转换为任意进制base
    convertstring="0123456789ABCDEF"
    if n<base:
        return convertstring[n]
    else:
        return toStr(n//base,base)+convertstring[n%base]    #将取整之后的结果进行递归调用，字符串进行相加是连接
print(toStr(415,16))
#递归可视化：Python内置的海龟作图系统turtle module
#画红色的正方形
# t=turtle.Turtle()   #作图开始
# t.pencolor('red')    #使用红色
# for i in range(4):
#     t.forward(100)   #指挥海龟作图前进100个单位
#     t.right(90)   #右转90度
# turtle.done()   #作图结束
#画分形树：树干、右边的小树、左边的小树，分形树是自相似递归图形
# def tree(branch_len):
#     if branch_len>5:   #树干太短就不画，即递归结束条件
#         t.forward(branch_len)   #画树干
#         t.right(20)    #往右倾斜20度
#         tree(branch_len-15)    #递归调用，画右边的小树树干减15
#         t.left(40)  #向左回40度，即左倾斜20度
#         tree(branch_len-15)    #递归调用，画左边的小树树干减15
#         t.right(20)  #向右回40度，即左倾斜20度
#         t.backward(branch_len)    #海龟后退回原始位置
# t=turtle.Turtle()
# t.left(90)
# t.penup()     #抬笔
# t.backward(100)
# t.pendown()    #放笔
# t.pencolor('green')
# t.pensize(2)
# tree(75)
# t.hideturtle()
# turtle.done()
   
#汉诺塔问题：在一个寺庙里，有三根柱子，其中一个套着64个由小到大的黄金盘片，现在需要把这一叠黄金盘从一根柱子搬到另一根，
#规则是：一次只能般一个盘子，大盘子不能叠在小盘子之上，一秒移动一个，完成任务需要五千亿年，是一个世界末日的问题
#可以转换成移动63，62，61......个盘片,最小问题是移动两个盘片
# def moveDish(height,frompole,withpole,topole):
#     if height>=1:
#         moveDish(height-1,frompole,withpole,topole)
#         moveDisk(height,frompole,topole)
#         moveDish(height-1,withpole,frompole,topole)
# def  moveDisk(disk,frompole,topole):
#     print(f"Moving disk[{disk}] from {frompole} to {topole}")
# moveDish(4,"#1","#2","#3")
    
#贪心策略（最最最），如自动贩卖机，找零一般要求最多数量的最大面值，每个货币体系的币值不一样，就有可能会失效
#动态规划解法(问题的最优解包含了更小规模问题的最优解，这是一个最优解问题能用动态规划策略解决的必要条件)
#从最简单的1分钱找零的最优解开始，逐步递加上去，设法保持每一分钱的递加都是最优解，直到需要我们的找零钱数
# def makeChange(coinValueList,change,minCoins):   #币值体系，找零数，所需的最少硬币数
#     #从一分开始到change逐个计算最小硬币数
#     for cents in range(1,change+1):
#         #初始化一个最大值
#         coincount=cents
#         #减去每个币值，向后查最少币值数，同时记录总得最小数
#         for j in [c for c in coinValueList if c<=cents]:
#             if minCoins[cents-j]+1<coincount:    #mincoins[]初始化是一个1*64的空列表
#                 coincount=minCoins[cents-j]+1
#             #得到当前最少币值数，记录到表中
#             minCoins[cents]=coincount
#             #返回最后一个结果
#     return minCoins[change]
# print(makeChange([1,5,10,21,25],63,[0]*64))
#博物馆大盗问题（打家劫舍）：博物馆有五件宝物，每件宝物有自己的重量和价值，大盗的背包仅能背负20公斤，大盗如何选择宝物，拿得到的价值最高


#顺序查找：查找某一项有没有出现在这个列表中
#有序表查找代码：给出的列表是按照从小到大或者从大到小的顺序排列的,还包括大小的比较，如果数据项不存在可以提前结束，O（n）
# def ordersearch(alist,item):
#     pos=0
#     find=False
#     stop=False
#     while pos<len(alist) and not find  and not stop:
#         if alist[pos]==item:
#             find=True
#         else:
#             if alist[pos]>item:
#                 stop=True
#             else:
#                 pos=pos+1
#     return find
# print(ordersearch([1,3,5,7,9,23,45,67],34))
#无序表查找代码：给出的列表是随机的排列的，要比对列表中的所有数据项，O（n）
# def unordersearch(alist,item):
#     pos=0
#     find=False
#     while pos<len(alist) and not find :
#         if alist[pos]==item:
#             find=True
#         else:
#             pos=pos+1
#     return find
# print(unordersearch([5,1,8,2,34,78,34,90],34))

#二分查找：从列表的中间开始对比，一般是有序表,O(logn)
# def binarySearch(alist,item):
#     first=0
#     last=len(alist)-1
#     find=False
#     while not find and first<=last:
#         midpos=(first+last)//2
#         if alist[midpos]==item:
#             find=True
#         else:
#             if alist[midpos]>item:
#                 last=midpos-1
#             else:
#                 first=midpos+1
#     return find
# print(binarySearch([1,5,7,9,23,45,67,89,90],9))

# 冒泡排序：通过相邻元素的比较来把来把小的放前面，大的放后面，第一趟对比就可以把最大的数放在最后面，第二趟对比就可以把第二大的数放在倒数第二的位置，O（n2）
# def bubbleSort(alist):
#     for passum in range(len(alist)-1,0,-1):
#         for i in range(passum):
#             if alist[i]>alist[i+1]:    #要保证i+1小于或等于最大的下标
#                 alist[i],alist[i+1]=alist[i+1],alist[i]
#     return  alist
# print(bubbleSort([1,4,7,2,9,11,6]))
#选择排序：第一趟对比将最大的数和最后一个数交换，第二趟对比将第二大的数和倒数第二个数交换
# def selectionSort(alist):
#     for fillsolt in range(len(alist)-1,0,-1):
#         positonmax=0
#         for location in range(1,fillsolt+1):
#             if alist[location]  > alist[positonmax]:
#                 positonmax=location
#         alist[positonmax],alist[fillsolt]=alist[fillsolt],alist[positonmax]
#     return alist
# print(selectionSort([1,4,7,2,9,11,6]))
# 插入排序算法：类似于起扑克牌的过程,O(n2)
# def insertsort(alist):
#     for index in range(1,len (alist)):
#         currentvalue=alist[index]    #currenvalue是从下标1开始的，就是需要插入的项，需要插入的项取出来当前位置为空
#         position=index
#         while position>0 and alist[position-1]>currentvalue:   #当前需要插入的项小于其前一项
#             alist[position]=alist[position-1]   #将前一项放到当前空的位置
#             position=position-1
#         alist[position]=currentvalue  #插入新项
#     return alist
# print(selectionSort([1,7,4,2,9,11,6]))
#谢尔排序：以插入排序作为基础，对无序表进行间隔划分子列表，，一般初始间隔为n/2,每个子列表都执行插入排序,后面间隔再缩小到n/4,n/8
# def shellsort(alist):
#     sublistcount=len(alist)//2   #间隔设定
#     while sublistcount>0:
#         for startposution in range(sublistcount):
#             gapInsrtionSort(alist,startposution,sublistcount)
#             print("after incremwnts of size",sublistcount,"this list is",alist)
#         sublistcount=sublistcount//2
# def gapInsrtionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):   #遍历的步长为对应的间隔，按照插入排序的原理排序
#         currentvalue=alist[i]
#         position=i
#         while position>=gap and alist[position-gap]>currentvalue:   #当前需要插入的项小于其前一项
#             alist[position]=alist[position-gap]   #将前一项放到当前空的位置
#             position=position-gap
#         alist[position]=currentvalue  
# print(shellsort([1,7,4,2,9,11,6]))
#归并排序MergeSort:先由大到小分开，再由小到大排序合并
def MergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]    #切片有左闭右开原则
        righthalf=alist[mid:]   #将列表分成左右两部分
        MergeSort(lefthalf)
        MergeSort(righthalf)   #递归调用



#二叉树的嵌套列表法
# binaryTree=[根，[根，[左]，[右]],[根，[左],[右]]]
#建立表达式解析树
def buildParseTree(fpexp):   #参数是字符串表达的全括号表达式
    fplist=fpexp.split()
    pStack=Stack()
    eTree=binaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i  in ['+','-','*','/']:
            currentTree.setRootVal(int(i))
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild() 
        elif i==')':
            currentTree=pStack.pop()
        else:
            raise ValueError
    return  eTree
    print(buildParseTree([['*'],['+','5','3'],['/','10','2']]))
            


print([0]*64)

        


