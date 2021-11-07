"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

1 <= n <= 11
"""

class Solution:
    def dicesProbability(self, n: int) -> list:
        """
        max_value = n * 6
        init prob(val, 1), val = 1 - max_value
        prob(val, n) = sum_i=1-6{prob(val-i, n-1)}
        """
        max_value = n * 6
        prob = [[0 for x in range(max_value + 1)] for y in range(n)]

        # initiation
        for val in range(1,7):
            prob[0][val] = float(1 / 6)
        
        # dp
        for dice in range(1,n):
            current_minval = dice + 1
            current_maxval = ( dice + 1 ) * 6
            for val in range(current_minval, current_maxval + 1):
                for i in range(6):
                    prob[dice][val] += prob[dice - 1][val - i - 1] * float(1 / 6)
        
        res = prob[n - 1][n : n * 6 + 1]
        return res

test = Solution()
n = 3
print([round(item, 5) for item in test.dicesProbability(n)])