"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
输入：x = 2.00000, n = 10
输出：1024.00000
输入：x = 2.10000, n = 3
输出：9.26100
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

理解快速幂的算法
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = float(1)
        if x == 0 or x == 1:
            return x
        if n < 0:
            n = -1 * n
            x = 1 / x
        while n:
            if n & 1:
                ans = ans * x
            n >>= 1
            x = x * x

        return ans