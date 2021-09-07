"""
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
"""

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sequence = [] # 维护一个升序序列
        self.seq_len = 0


    def addNum(self, num: int):
        """
        :type num: int
        :rtype: None
        """
        self.sequence.append(num)
        idx = self.seq_len
        while idx > 0:
            i
        


    def findMedian(self) -> float:
        """
        :rtype: float
        """
        if self.seq_len == 0:
            return []
        else:
            if self.seq_len % 2 == 0:
                median_idx1 = int(self.seq_len / 2)
                median_idx2 = int(self.seq_len / 2) + 1



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
