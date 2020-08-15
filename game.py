# print("-"*30,"欢迎进入游戏","-"*30)
# username=input("请输入用户名：")
# money=0
# answer=input("确定进入游戏吗(y/n)?")

# if answer == y:
#     #判断游戏币是否充足
#     while money<2:
#         n=input("金币不足，请充值：")
#         if n%100==0 and n>0:
#             money=(n//100)*30
#     print("当前金币：")
#     print("进入游戏...............")

#     while True:
#         t1=random.randint(1.6)
#         t2=random.randint(1,6)
#         money-=2
#         guess=input("当前洗牌完毕，请猜大小(大/小)：")
#         if ((t1+t2)>6 and guess=="大") or ((t1+t2)<6 and guess=="小"):
#             print("猜大小正确，奖励一枚金币")
#             money+=1
#         else:
#             print("很遗憾，本局游戏输了！")
#         answer=input("是否继续下一局(y/n)：")
#         if answer =='n' or money<2:
#             print("无法继续游戏")
#             break
# else:
#     print("不进入游戏")
