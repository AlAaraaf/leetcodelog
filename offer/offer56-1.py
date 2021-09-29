"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

2 <= nums.length <= 10000
"""

class Solution:
    def singleNumbers(self, nums: list) -> list:
        
        ListLen = len(nums)
        TotalXor = nums[0] ^ nums[1]

        if ListLen == 2 and TotalXor == 0:
            return nums
        
        for i in range(2,ListLen):
            TotalXor ^= nums[i]
        
        SplitNum = 1
        while not SplitNum & TotalXor:
            SplitNum <<= 1
        
        a = 0
        b = 0
        for number in nums:
            if number & SplitNum:
                a ^= number
            else:
                b ^= number
        
        return [a,b]

test = Solution()
nums = [1,1,2,3,4,4]
print(test.singleNumbers(nums))