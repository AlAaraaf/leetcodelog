"""
给你一个整数数组coins，表示不同面额的硬币；以及一个整数amount，表示总金额。
计算并返回可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回-1。
你可以认为每种硬币的数量是无限的。

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

输入：coins = [2], amount = 3
输出：-1

输入：coins = [1], amount = 0
输出：0

输入：coins = [1], amount = 1
输出：1

输入：coins = [1], amount = 2
输出：2
"""

class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        # 边界判断
        if amount == 0:
            return 0
        coins = sorted(coins)
        if amount < coins[0]:
            return -1
        
        # dp - n[amount] = min(n[amount-coin[i]+1]) iter i
        Numbers = [float("inf")] * (amount + 1)
        Numbers[0] = 0
        
        for i in range(coins[0], amount + 1):
            CurrentMin = float("inf")
            for j in coins:
                if i - j >= 0:
                    CurrentMin = min(CurrentMin, Numbers[i - j] + 1)
            Numbers[i] = CurrentMin

        if Numbers[amount] != float("inf"):
            return Numbers[amount]
        else:
            return -1

test = Solution()
coins = [2,4,6,8]
amount = 11
print(test.coinChange(coins, amount))