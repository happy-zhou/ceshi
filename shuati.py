from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque
# 例子1：两数之和——给定一个整数数组nums和一个目标值target，请在该数组中找出和为目标值的那两个整数，并返回这两个数的下标
# def search(nums,target):
#     for num in nums:
#         r=target-num
#         if r in nums and r!=num:
#             a=nums.index(num)
#             b=nums.index(r)
#             return [a,b]
# print(search([1,2,3,4,7,9],17))

# def twosum(nums,target):
#     lens=len(nums)
#     j=-1
#     for i in range(1,lens):
#         temp=nums[:i]
#         if (target-nums[i]) in temp:
#             j=temp.index(target-nums[i])
#             break
#     if j>0:
#         return [i,j]
# print(twosum([1,2,3,4,7,9],16))

# 例子2：给出一个32位的有符号整数，将这个整数上中每位上的数字进行反转
# def reverse(x):
#     if -10<x<10:
#         return x
#     str1=str(x)    #将整形转换成字符串类型
#     if str1[0]!='-':
#         str1=str1[::-1]    #########################将此字符串逆序
#         x=int(str1)
#     else:
#         str1=str1[:0:-1]
#         x=int(str1)
#         x=-x
#     return x if -1256236323<x<1256236323 else 0
# print(reverse(-123))


# #例子三：判断一个整数是否是回文数
# 可采用双端队列,比较队首队尾出来的元素是否相等
# 也可将整数逆序，比较逆序与未逆序的是否相等
# def huiwenshu(nums):
#     nums=str(nums)
#     d=Deque()
#     rem=True
#     for num in nums:
#         d.addRear(num)
#     while d.size()>1:
#         first=d.removeFront()
#         last=d.removeRear()
#         if first!=last:
#             rem=False
#     return rem
# print(huiwenshu(-123))


# 例子4：非空字符串全部由大写字母组成，求出每个字母在这个字符串中出现的次数
# def tongji(str):
#     lens=len(str)
#     str1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     num=0
#     for i in range(len(str)-1):
#         for j in range(0,len(str1)):
#             if str[i]==str1[j]:
#                 num=num+1
#         return str[i]=num
# print(tongji('AFVBHYIO'))

#例子5：任意给定一个字符串，58神奇串要求字符的取值范围是[5,8]，找出最长的58神奇串
# def shenqi(str1):
#     lens=len(str1)
#     res=''
#     for i in range(lens-1):
#         if str1[i]==5 or str1[i]==8:
#             res=str1[i]
#             if str1[i+1]==5 or str1[i+1]==8:
#                 res=res+str1[i+1]
#             else:
#                 return res
# print(shenqi('13584853'))



# #例子6：一叠钞票，面值包含1，5，10，20，50，100，每次可以从顶部或底部抽出一张钞票，最多可抽五次，求抽出的最大金额和
# def maxValue(list1):
#     lens=len(list1)
#     sum=0
#     for i in range(5):

# 例子7：20题----有效的括号：给定一个只包括大中小括号的字符串，判断该字符串是否有效，要求：左括号必须以相同类型的右括号闭合，左右括号必须以正确的顺序闭合
# 括号匹配可以联想到键值对-字典
# def kuohao(s: str):
#         match_dic = {')':'(', ']':'[', '}':'{'}
#         temp_list = []    #此时列表也可用栈的功能来实现

#         for ch in s:
#             if ch in '([{':
#                 temp_list.append(ch)
#             elif ch in ')]}':
#                 # 若右括号比左括号先出现,此时列表为空， 不能匹配闭合
#                 if not temp_list:   #空列表相当于false
#                     return False
#                 # 遇到右括号, 必然要与上一个左括号闭合, 如果不匹配就 False
#                 if match_dic[ch] == temp_list[-1]:
#                     temp_list.pop(-1)
#                 else:
#                     return False
#         # 正常闭合的情况下, 栈里面应该全都弹出去了, 所以应该是空的
#         if not temp_list:
#             return True
#         else:
#             return False
# print(kuohao('()[]{'))
# def kuohao(s: str):
#         match_dic = {')':'(', ']':'[', '}':'{'}  #右括号，后出现的作为键，早出现的左括号作为值
#         s1=Stack()   
#         for ch in s:
#             if ch in '([{':
#                 s1.push(ch)
#             elif ch in ')]}':
#                 # 右括号比左括号先出现, 不能闭合
#                 if s1.isEmpty():   #空列表相当于false
#                     return False
#                 # 遇到右括号, 必然要与上一个左括号闭合, 如果不匹配就 False
#                 if match_dic[ch] == s1.pop():
#                     pass     #pass占位符
#                 else:
#                     return False
#         # 正常闭合的情况下, 栈里面应该全都弹出去了, 所以应该是空的
#         if s1.isEmpty():
#             return True
#         else:
#             return False
# print(kuohao('()[]{'))

# 例子7：53.最大子序和-----给定一个整数数组，找到一个具有最大和的连续子数组（子数组最少包含一个元素)，返回最大和
# def maxSubSum(nums):
#     lens=len(nums)
#     tem=nums[0]     #当前和
#     maxsum=tem
#     if lens==1:
#         return maxsum
#     for i in range(1,lens):
#         if tem+nums[i]>nums[i]:   # 当前序列加上此时的元素值大于当前的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
#             maxsum=max(maxsum,tem+nums[i])
#             tem=tem+nums[i]
#         else:    #当tmp(当前和)小于下一个元素时，当前最长序列到此为止,以该元素为起点继续找最大子序列,
#             maxsum=max(maxsum,tem,tem+nums[i],nums[i])
#             tem=nums[i]
#     return maxsum
# print(maxSubSum([-1,3,8,-5,9,-4,9]))

# 例子8：70.爬楼梯：每次可以爬1或两个台阶，需要n阶才能到达楼顶，问有多少种方法可以到达楼顶
# def climbStairs(n):
#     #爬到n楼f(n)为n-1楼和n-2楼方法数之和，原因：第一次只跳一级，剩下的n-1级共有f(n-1)种方法；第一次跳两级，剩下的n-2级共有f(n-2)种方法
#     fir=1
#     sec=2
#     res=0
#     for i in range(3,n+1):
#         res=fir+sec
#         fir=sec
#         sec=res
#     return max(res,n)     #此种方式包括了n为1和2的情况
# print(climbStairs(5))

# 例子9：21.合并两个有序链表：将两个升序链表合并为一个新的升序链表返回(不太懂)
# def merTwoLists(l1,l2):
#     if not l1: return l2  # 终止条件，直到两个链表都空
#         if not l2: return l1
#         if l1.val <= l2.val:  # 递归调用
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2
    

# 例子9：判断一个二叉树是否为对称二叉树
# #对称二叉树的性质：左子树的前序遍历和右子树的后续遍历是互为逆序的关系


# 例子10：买卖股票的最佳时机：给定一个数组，第i个元素是该股票第i天的价格，买入和卖出只能一次，求所能获取的最大利润

# def maxProfit(self, prices: List[int]) -> int:
#     lens=len(prices)
#     maxval=0
#     for i in range(lens-1):
#         for j in range(i+1,lens):
#             val=prices[j]-prices[i]
#             if val>maxval:
#                 maxval=val
#     return maxval           #结果提示超出时间限制
# 解法2：动态规划，用一个数组存放前i天的最大利润，而前i天的最大利润是和前i-1天的最大利润以及第i天的价格有关的，那么数组的最后一个元素就是最大利润
# def maxProfit(prices):
#     n=len(prices)
#     dp=[0]*n
#     minprice=prices[0]
#     if n==0:
#         return 0
#     for i in range(1,n):   #从第二天开始算利润
#         minprice=min(minprice,prices[i])
#         dp[i]=max(dp[i-1],prices[i]-minprice)
#     return dp[-1]
# print(maxProfit([2,4,7,1,9,4]))

# 例子11：非递归阶乘：输入n,不采用递归的方法输出其阶乘
# def jiecheng(num:int):
#     multi=1
#     while num >=1:
#         multi=multi*num
#         num=num-1
#     return multi
# print(jiecheng(4))





    


        
