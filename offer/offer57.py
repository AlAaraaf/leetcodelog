"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。
"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        
        listLen = len(nums)
        lidx = 0
        ridx = listLen - 1
        currentSum = nums[lidx] + nums[ridx]
        
        while lidx < ridx and currentSum != target:
            if currentSum < target:
                lidx += 1
            if currentSum > target:
                ridx -= 1
            currentSum = nums[lidx] + nums[ridx]
        
        return [nums[lidx], nums[ridx]]

test = Solution()
nums = [10,26,30,31,47,60]
target = 40
print(test.twoSum(nums, target))