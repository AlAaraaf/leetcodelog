"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

0 < grid.length <= 200
0 < grid[0].length <= 200

动态规划 - maxvalue[i,j] = max(maxvalue[i-1,j],maxvalue[i,j-1]) + value[i,j]
"""

class Solution:
    def maxValue(self, grid: list) -> int:
        Width = len(grid[0])
        Length = len(grid)

        maxValue = [[0 for x in range(Width)] for y in range(Length)]
        maxValue[0][0] = grid[0][0]

        for i in range(1, Length):
            maxValue[i][0] = maxValue[i - 1][0] + grid[i][0]

        for j in range(1, Width):
            maxValue[0][j] = maxValue[0][j - 1] + grid[0][j]
        
        for i in range(1, Length):
            for j in range(1, Width):
                maxValue[i][j] = max(maxValue[i - 1][j], maxValue[i][j - 1]) + grid[i][j]

        return maxValue[Length - 1][Width - 1]

test = Solution()
grid = [[1,3,1], [1,5,1], [4,2,1]]
print(test.maxValue(grid))