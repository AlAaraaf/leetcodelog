"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
"""

class Solution:
    def maxSubArray(self, nums: list) -> int:
        """
        dp: maxsub[i] = max(maxsub[i-1]+nums[i], nums[i], maxsub[i-1])
        """
        listLen = len(nums)
        maxSub = [float('-Inf') for item in range(listLen)]

        maxSub[0] = nums[0]
        for i in range(1, listLen):
            maxSub[i] = max(maxSub[i-1] + nums[i], nums[i])
        
        return max(maxSub)

test = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(test.maxSubArray(nums))