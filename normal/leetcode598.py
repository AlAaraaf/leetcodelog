"""
给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。

操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，
含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。

在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: list) -> int:
        h_min = m
        v_min = n
        for op in ops:
            if op[0] and op[1]:
                h_min = min(h_min, op[0])
                v_min = min(v_min, op[1])
        return h_min * v_min
        
test = Solution()
m = 3
n = 3
operations = [[2,2],[3,3]]
print(test.maxCount(m,n,operations))