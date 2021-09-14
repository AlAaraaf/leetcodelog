"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1

递推获得最终结果

之后可使用矩阵快速幂法重新解一次
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        MOD = 1000000007
        pre1 = 1
        pre2 = 0
        ans = 0
        for i in range(2,n+1):
            ans = (pre1 + pre2) % MOD
            pre2 = pre1
            pre1 = ans
        
        return ans
        
test = Solution()
n = 6
print(test.fib(n))