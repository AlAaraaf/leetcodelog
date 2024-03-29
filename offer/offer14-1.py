"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
2 <= n <= 58
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        # 边界判断
        if n < 4:
            if n == 1 or n == 2:
                return 1
            return 2
        
        # 大于4的正数n必被拆分
        MaxResult = [0] * (n + 1)
        for i in range(1,n + 1):
            if i <= 4:
                MaxResult[i] = i
            else:
                MaxResult[i] = max(MaxResult[i-4]*4, MaxResult[i-3]*3, MaxResult[i-2]*2, MaxResult[i-1]*1)
        
        return MaxResult[n]