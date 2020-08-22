from multiprocessing import  Process
from time import sleep

def task1():
    while True:
        sleep(1)
        print('这就是任务1')

def task2():
    while True:
        sleep(2)
        print('这就是任务2')
#process=Process(target=函数，name=进程的名字，args=(给函数传递的参数))，process是一个对象
p1=Process(target=task1,name='任务1',args=(1,'aa'))
p1.run()                   #run只是执行了任务但是并没有启动进程，因此只有执行了第一个任务之后才会执行第二个任务
p2=Process(target=task2)
p2.run()
p2.start()       #strat是启动进程并执行任务
p2.terminate()   #terminate终止进程



# 进程池：如果要创建上百甚至上千个进程，手动创建工作量巨大，此时可以用到multiprocessing模块提供的pool方法，
# 初始化pool时可以指定一个最大的进程数，当有新的请求提交到pool时，池没有满就会创建一个新的进程来执行该请求；
# 但如果池已经到容纳的最大值，新的请求就会等待，直到池中有进程结束，才会创建新的进程来执行

#进程间的通信