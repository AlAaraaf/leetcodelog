"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1
每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

由于2<=n<=1000，直接使用动态规划会超时
改用贪心算法，尽量拆成3的乘积
"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        ans = 1
        MOD = 1000000007
        while n > 4:
            ans = (ans * 3) % MOD 
            n = n - 3
        ans = ans * n
        return ans % MOD

test = Solution()
n = 10
print(test.cuttingRope(n))