# 区分父子进程
import os
import time

res = os.fork()
print(f'res == {res}')

if res == 0:
    print(f'我是子进程，我的pid是：{os.getpid()}，我的父进程id是：{os.getppid()}')
else:
    print(f'我是父进程，我的pid是：{os.getpid()}')

# fork()运行时，会有两个返回值，当其大于0时，此进程为父进程，且返回的pid为子进程的pid；
# 父进程和子进程并不会随着对方的结束而立刻结束
