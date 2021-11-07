"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
"""

class Solution:
    def maxProfit(self, prices: list) -> int:
        
        listLen = len(prices)
        
        if listLen == 0:
            return 0
        
        suff_maxval = [0 for item in range(listLen)]
        suff_maxval[-1] = prices[-1]
        
        # iter1
        for idx in range(1, listLen):
            suff_maxval[listLen - idx - 1] = max(suff_maxval[listLen - idx], prices[listLen - idx - 1])
        
        # iter2
        max_profit = 0
        for idx in range(listLen):
            if suff_maxval[idx] - prices[idx] > max_profit:
                max_profit = suff_maxval[idx] - prices[idx]
        
        return max_profit

test = Solution()
prices = [7,6,4,3,1]
print(test.maxProfit([]))