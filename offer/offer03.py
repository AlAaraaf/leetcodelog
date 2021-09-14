"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

输入：[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
限制 2 <= n <= 100000

解法1 - 哈希表
解法2 - 原地哈希（使用for循环的时候会报错，因为会漏掉一些不能+1的条件）a
"""
class Solution:
    def findRepeatNumber1(self, nums: list) -> int:
        dict = {}
        for number in nums:
            if number not in dict.keys():
                dict[number] = 1
            else:
                return number
    
    def findRepeatNumber2(self, nums: list) -> int:
        seq_len = len(nums)
        i = 0
        while i < seq_len:
            if nums[i] != i:
                if nums[nums[i]] != nums[i]:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                else:
                    return nums[nums[i]]
            else:
                 i += 1
        return -1

test = Solution()
nums = [3,4,2,0,0,1]
print(test.findRepeatNumber1(nums))
print(test.findRepeatNumber2(nums))