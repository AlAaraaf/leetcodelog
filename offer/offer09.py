"""
用两个栈实现一个队列。
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

一个栈负责输入，一个栈负责输出
"""

class CQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if len(self.outStack) == 0:
            if len(self.inStack) == 0:
                return -1
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

obj = CQueue()
value = 1
obj.appendTail(value)
print(obj.deleteHead())