"""
峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组 nums，找到峰值元素并返回其索引。
数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞。

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
"""
from typing import Sequence


class Solution:
    def findPeakElement(self, nums: list) -> int:
        # 边界判断
        sequence_length = len(nums)
        if sequence_length == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        # 二分法查找峰值
        start_idx = 0
        end_idx = sequence_length - 1
        mid = int((start_idx + end_idx) / 2)

        while start_idx < end_idx:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                break
            
            #中点比左侧低，峰值可能在左侧
            elif nums[mid] < nums[mid - 1]:
                end_idx = mid - 1
                mid = int((start_idx + end_idx) / 2)
            
            # 中点比右侧低，峰值可能在右侧
            else:
                start_idx = mid + 1
                mid = int((start_idx + end_idx) / 2)
        
        return mid


solution = Solution()
nums = [1,2,3,2]
print(solution.findPeakElement(nums))