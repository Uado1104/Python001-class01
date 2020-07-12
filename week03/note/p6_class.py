# 面向对象的调试方法
import os
import time
from multiprocessing import Process

# 继承Process类创建一个新类
class NewProcess(Process):
    def __init__(self,num):
        self.num = num 
        super().__init__()

    # 重写Process类中的run方法。
    def run(self):
        while True:
            print(f'我是进程{self.num}，我的pid是：{os.getpid()}')
            time.sleep(1)

for i in range(2):
    p = NewProcess(i)
    p.start()
# 当不给Process指定target时，会默认调用Process类里的run()方法。
# 这和指定target效果是一样的，只是将函数封装进类之后便于理解和调用。