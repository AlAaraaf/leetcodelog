"""
给定一个正整数n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。返回你可以获得的最大乘积。

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""

class Solution:
    def integerBreak(self, n: int) -> int:
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

test = Solution()
n = 10
print(test.integerBreak(n))