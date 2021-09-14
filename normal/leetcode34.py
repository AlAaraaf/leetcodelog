"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
输入：nums = [], target = 0
输出：[-1,-1]

执行1：执行出错： index out of range {[1],1} 边界维护没有做好
执行2：解答错误：二分查找的终止条件应该有两处：1 区间只包含一个值 2 成功找到目标值
执行3：解答正确
"""
import sys
class Solution:
    def searchRange(self, nums: list, target: int) -> list:        
        # 边界判断
        if len(nums) == 0:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        # 二分查找初始值
        start_idx = 0
        end_idx = len(nums) - 1
        sequence_length = end_idx + 1
        mid = int((start_idx + end_idx) / 2)

        while (start_idx < end_idx):
            if nums[mid] < target:
                start_idx = mid + 1
                mid = int((start_idx + end_idx) / 2)
            elif nums[mid] > target:
                end_idx = mid - 1
                mid = int((start_idx + end_idx) / 2)
            else:
                break

        # 左右增长
        if nums[mid] != target:
            return [-1, -1]
        
        left_boundary = mid
        right_boundary = mid
        while (left_boundary - 1 >= 0 and nums[left_boundary - 1] == target):
            left_boundary -= 1
        while (right_boundary + 1 < sequence_length and nums[right_boundary + 1] == target):
            right_boundary += 1
    
        return [left_boundary,right_boundary]

solution = Solution()
nums = [1]
target = 1
print(solution.searchRange(nums, target))
