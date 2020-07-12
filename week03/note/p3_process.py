from multiprocessing import Process
def f(name):
    print(f'hello{name}')

if __name__ == '__main__':
    p = Process(target=f,args=('join',))
    # 将函数对象f传给target，如果是f()的话，就是将函数执行的结果传给target
    # "'join',"中的,表示join为元组，去掉的话表示join为字符串

    p.start()
    p.join()
# join([timeout])
# 如果可选参数timeout为None，默认值，则该方法将阻塞。
# 直接调用join()方法的进程终止，如果timeout为正数，则最多会阻塞timeout秒。
# 如果进程终止或方法超时，则该方法返回None。
# 检查进程的exitcode以确定它是否会终止。
# 一个进程可以合并多次。
# 进程无法并入自身，因为这会导致死锁。
# 不可在尝试启动进程之前合并进程