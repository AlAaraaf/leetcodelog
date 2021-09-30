"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

1 是丑数
n 不超过1690
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        numList = [1]
        listIdx = 0

        multiByItem = [[2],[3],[5]]
        multiItem = [2,3,5]

        def minItem(multiList) -> int:
            x1 = multiList[0][-1] if len(multiList[0]) else float("Inf")
            x2 = multiList[1][-1] if len(multiList[1]) else float("Inf")
            x3 = multiList[2][-1] if len(multiList[2]) else float("Inf")

            if x1 <= x2 and x1 <= x3:
                return 0
            elif x2 <= x1 and x2 <= x3:
                return 1
            elif x3 != float("Inf"):
                return 2
            else:
                return 3

        while listIdx < n - 1:
            minIdx = minItem(multiByItem)
            maxValue = max(multiByItem[0][-1], multiByItem[1][-1], multiByItem[2][-1])
            minValue = multiByItem[minIdx].pop(-1)
            
            if minValue != numList[-1]:
                numList.append(minValue)
                listIdx += 1
            
            if numList[listIdx] * 2 <= maxValue:
                for i in range(3):
                    multiByItem[i].insert(0, numList[listIdx] * multiItem[i])
            
            print(minValue, multiByItem)
            
        return numList[n-1]

test = Solution()
n = 6
print(test.nthUglyNumber(n))