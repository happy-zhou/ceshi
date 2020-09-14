
from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque
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

#递归数列求和
# def listsum(numlist):
#     if len(numlist)==1:
#         sum=numlist[0]
#     else:
#         return numlist[0]+listsum(numlist[1:])
# print(listsum([1,3,5,7,9]))
#汉诺塔问题：在一个寺庙里，有三根柱子，其中一个套着64个由小到大的黄金盘片，现在需要把这一叠黄金盘从一根柱子搬到另一根，
# 规则是：一次只能般一个盘子，大盘子不能叠在小盘子之上，一秒移动一个，完成任务需要五千亿年，是一个世界末日的问题
# def moveDish(height,frompole,withpole,topole):
#     if height>=1:
#         moveDish(height-1,frompole,withpole,topole)
#         moveDisk(height,frompole,topole)
#         moveDish(height-1,withpole,frompole,topole)
# def  moveDisk(disk,frompole,topole):
#     print(f"Moving disk[{disk}] from {frompole} to {topole}")
# moveDish(4,"#1","#2","#3")
    
#贪心策略（最最最），如自动贩卖机，找零一般要求最多数量的最大面值，每个货币体系的币值不一样，就有可能会失效
#动态规划解法(问题的最优解包含了更小规模问题的最优解，这是一个都最优解问题能用动态规划策略解决的必要条件)
def makeChange(coinValueList,change,minCoins):   #币值体系，找零数，所需的最少硬币数
    #从一分开始到change逐个计算最小硬币数
    for cents in range(1,change+1):
        #初始化一个最大值
        coincount=cents
        #减去每个币值，向后查最少币值数，同时记录总得最小数
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coincount:
                coincount=minCoins[cents-j]+1
            #得到当前最少币值数，记录到表中
            minCoins[cents]=coincount
            #返回最后一个结果
    return minCoins[change]
print(makeChange([1,5,10,21,25],63,[0]*64))
#博物馆大盗问题：博物馆有五件宝物，每件宝物有自己的重量和价值，大盗的背包仅能背负20公斤，大盗如何选择宝物，拿得到的价值最高


#顺序查找：查找某一项有没有出现在这个列表中
#有序表查找代码：给出的列表是按照从小到大或者从大到小的顺序排列的,还包括大小的比较，如果数据项不存在可以提前结束，O（n）
def ordersearch(alist,item):
    pos=0
    find=False
    stop=False
    while pos<len(alist) and not find  and not stop:
        if alist[pos]==item:
            find=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos=pos+1
    return find
print(ordersearch([1,3,5,7,9,23,45,67],34))
#无序表查找代码：给出的列表是随机的排列的，要比对列表中的所有数据项，O（n）
def unordersearch(alist,item):
    pos=0
    find=False
    while pos<len(alist) and not find :
        if alist[pos]==item:
            find=True
        else:
            pos=pos+1
    return find
print(unordersearch([5,1,8,2,34,78,34,90],34))

#二分查找：从列表的中间开始对比，一般是有序表,O(logn)
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    find=False
    while not find and first<=last:
        midpos=(first+last)//2
        if alist[midpos]==item:
            find=True
        else:
            if alist[midpos]>item:
                last=midpos-1
            else:
                first=midpos+1
    return find
print(binarySearch([1,5,7,9,23,45,67,89,90],9))

# 冒泡排序：通过相邻元素的比较来把来把小的放前面，大的放后面，第一趟对比就可以把最大的数放在最后面，第二趟对比就可以把第二大的数放在倒数第二的位置，O（n2）
def bubbleSort(alist):
    for passum in range(len(alist)-1,0,-1):
        for i in range(passum):
            if alist[i]>alist[i+1]:    #要保证i+1小于或等于最大的下标
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return  alist
print(bubbleSort([1,4,7,2,9,11,6]))
#选择排序：第一趟对比将最大的数和最后一个数交换，第二趟对比将第二大的数和倒数第二个数交换
def selectionSort(alist):
    for fillsolt in range(len(alist)-1,0,-1):
        positonmax=0
        for location in range(1,fillsolt+1):
            if alist[location]  > alist[positonmax]:
                positonmax=location
        alist[positonmax],alist[fillsolt]=alist[fillsolt],alist[positonmax]
    return alist
print(selectionSort([1,4,7,2,9,11,6]))
# 插入排序算法：类似于起扑克牌的过程
def insertsort(alist):
    for index in range(1,len (alist)):
        currentvalue=alist[index]
        position=index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
    return alist
print(selectionSort([1,7,4,2,9,11,6]))
#谢尔排序：



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
            




        


