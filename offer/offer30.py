"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数
在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack == []:
            self.minStack.append(x)
        elif x <= self.minStack[-1]:
            self.minStack.append(x)


    def pop(self) -> None:
        if self.stack == []:
            return
        pop_value = self.stack.pop()
        if pop_value == self.minStack[-1]:
            self.minStack.pop()


    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]


    def min(self) -> int:
        if self.minStack != []:
            return self.minStack[-1]
        return -1



# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.min())
minStack.pop()
print(minStack.top())
print(minStack.min())