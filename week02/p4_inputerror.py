# 自定义一个异常类，继承Exception类
class UserInputError(Exception):
    # __init__函数在类刚一执行时就运行，ErroInfo用作错误信息的返回
    def __init__(self,ErroInfo):
        super().__init__(self,ErroInfo)
        self.errorinfo = ErroInfo
    # 魔术方法，使得类像字符串一样去使用
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if(not userinput.isdigit()):
        # 抛出异常
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
# 无论程序错误有无捕获，都执行,把使用的内存清理掉。
finally:
    del userinput