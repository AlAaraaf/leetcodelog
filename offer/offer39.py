"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

class Solution:
    def majorityElement(self, nums: list) -> int:
        index = {}
        listLen = len(nums)
        
        for i in range(listLen):
            index[nums[i]] = index.get(nums[i], 0) + 1
            if index[nums[i]] > listLen // 2:
                return nums[i]

test = Solution()
nums = [2,2,1,1,1,2,2]
print(test.majorityElement(nums))