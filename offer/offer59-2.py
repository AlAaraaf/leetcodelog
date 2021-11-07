"""
请定义一个队列并实现函数 max_value 得到队列里的最大值
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.prefixQueue = []

    def max_value(self) -> int:
        return self.prefixQueue[0] if self.prefixQueue != [] else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.prefixQueue != [] and self.prefixQueue[-1] < value:
            self.prefixQueue.pop()
        self.prefixQueue.append(value)

    def pop_front(self) -> int:
        if self.queue == []:
            return -1
        pop_value = self.queue.pop(0)
        if self.prefixQueue != [] and pop_value == self.prefixQueue[0]:
            self.prefixQueue.pop(0)
        return pop_value

# Your MaxQueue object will be instantiated and called as such:

input_str = ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
input_val = [[],[1],[2],[],[],[]]


for idx in range(len(input_str)):
    if input_str[idx] == 'MaxQueue':
        print('null')
        obj = MaxQueue()
    elif input_str[idx] == 'max_value':
        print(obj.max_value())
    elif input_str[idx] == 'push_back':
        print('null')
        obj.push_back(input_val[idx][0])
    else:
        print(obj.pop_front())