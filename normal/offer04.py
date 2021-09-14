"""
在一个n*m的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

HINT 双向有序问题类似梯度（只要向一个方向走就可以了）
"""


class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        # 边界判断
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # 向左减小，向下增大
        row_idx = 0
        col_idx = len(matrix[0]) - 1
        while row_idx < len(matrix) and col_idx >= 0:
            # print("current position: ({0},{1})".format(row_idx + 1, col_idx + 1))
            if target == matrix[row_idx][col_idx]:
                break
            elif target < matrix[row_idx][col_idx]:
                col_idx -= 1
            else:
                row_idx += 1
        
        if row_idx < len(matrix) and col_idx >= 0 and target == matrix[row_idx][col_idx]:
            return True
        else:
            return False

test = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
print(test.findNumberIn2DArray(matrix,20))