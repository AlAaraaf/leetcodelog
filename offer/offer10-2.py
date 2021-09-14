"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

输入：n = 2 | 输出：2
输入：n = 7 | 输出：21
输入：n = 0 | 输出：1

0 <= n <= 100
动态规划 f(n) = f(n - 2) + f(n - 1)
"""
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        pre1 = 2
        pre2 = 1
        ans = 0
        MOD = 1000000007
        for i in range(2,n):
            ans = (pre1 + pre2) % MOD
            pre2 = pre1
            pre1 = ans
        
        return ans

test = Solution()
n = 5
print(test.numWays(n))