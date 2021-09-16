"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格
不能移动到方格外，也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，
机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

输入：m = 2, n = 3, k = 1
输出：3
输入：m = 3, n = 1, k = 0
输出：1
1 <= n,m <= 100
0 <= k <= 20

简单递推
好几次出错的原因： 对判断canVisit的条件逻辑没有理清；除计算结果转整数的位置错误(应该直接用整除)
"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        
        canVisit = [[0 for x in range(n)] for y in range(m)]

        def getCount(x,y):
            # print("{0},{1} - {2}".format(x,y,int((x / 10) + (x % 10) + (y / 10) + (y % 10))))
            return (x // 10) + (x % 10) + (y // 10) + (y % 10)

        count = 0
        for x in range(m):
            for y in range(n):
                moveFromLeft = (x - 1 >= 0 and canVisit[x-1][y]) or (x,y) == (0,0)
                moveFromBottom = (y - 1 >= 0 and canVisit[x][y-1]) or (x,y) == (0,0)
                if moveFromLeft or moveFromBottom:
                    canVisit[x][y] = int(getCount(x,y) <= k)
                count += canVisit[x][y]
        return count

test = Solution()
print(test.movingCount(11,8,16))