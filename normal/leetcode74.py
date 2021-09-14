"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""
class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        m_length = len(matrix)
        n_length = len(matrix[0])
        # 边界判定
        # 若m=n=1，矩阵只有一个值，直接判断大小
        if m_length == 1 and n_length == 1:
            return matrix[0][0] == target
        # 判断目标值是否在矩阵范围内
        if matrix[0][0] > target or matrix[m_length - 1][n_length - 1] < target:
            return False

        # 二分法定位目标值所在行
        start_idx = 0
        end_idx = m_length - 1
        mid_row = int((start_idx + end_idx) / 2)

        while start_idx < end_idx:
            if matrix[mid_row][0] == target:
                return True
            
            # 比中点小，在前序行中
            if matrix[mid_row][0] > target:
                end_idx = mid_row - 1
                mid_row = int((start_idx + end_idx) / 2)
            
            # 比中点大，在当前行或后序行中，使用当前行末尾元素辅助进行判断
            if matrix[mid_row][0] < target:
                if matrix[mid_row][-1] >= target:
                    break
                else:
                    start_idx = mid_row + 1
                mid_row = int((start_idx + end_idx) / 2)
        
        # 二分法判断目标是否在当前行中
        # 边界判断
        if matrix[mid_row][0] > target or matrix[mid_row][-1] < target:
            return False
        if n_length == 1:
            return matrix[mid_row][0] == target
        
        start_idx = 0
        end_idx = n_length - 1
        mid_col = int((start_idx + end_idx) / 2)
        while start_idx < end_idx:
            if matrix[mid_row][mid_col] == target:
                return True
            
            # 比中点大，在后半部分
            if matrix[mid_row][mid_col] < target:
                start_idx = mid_col + 1
                mid_col = int((start_idx + end_idx) / 2)
            
            # 比中点小，在前半部分
            if matrix[mid_row][mid_col] > target:
                end_idx = mid_col - 1
                mid_col = int((start_idx + end_idx) / 2)
        
        return matrix[mid_row][mid_col] == target

solution = Solution()
matrix = [[1],[2],[3]]
target = 2
print(solution.searchMatrix(matrix, target))