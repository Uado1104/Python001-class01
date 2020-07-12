# Queue类是近似queue.Queue的克隆
# 现在的需求为：当我们有两个进程，一个负责写(write)另一个负责读(read)
# 当写的进程写完某部分以后要把数据交给读的进程进行使用
# write()将写完的数据交给队列，再由队列交给read()
from multiprocessing import Process,Queue

def f(q):
    q.put([42,None,'Hello'])

if __name__ == '__main__':
    # 需要设定队列的最大长度
    q = Queue()
    
    p = Process(target=f,args=(q,))
    p.start()
    # get时判断blocked是否为阻塞状态
    # 当blocked为True，判断time，当过了5秒后blocked依然为True，queue为空，抛出Queue.empty异常
    print(q.get())
    p.join()

# 队列是线程和进程安全的