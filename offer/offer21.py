"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
"""

class Solution:
    def exchange(self, nums: list) -> list:
        listLen = len(nums)
        if listLen == 0:
            return []

        lidx = 0
        ridx = listLen - 1
        while lidx < listLen and ridx >= 0 and lidx < ridx:
            
            # find even number in left part
            while lidx < listLen and nums[lidx] % 2 != 0:
                lidx += 1
            
            # find odd number in right part
            while ridx >= 0 and nums[ridx] % 2 == 0:
                ridx -= 1
            
            if lidx >= ridx:
                return nums
            else:
                temp = nums[lidx]
                nums[lidx] = nums[ridx]
                nums[ridx] = temp
            
            lidx += 1
            ridx -= 1
        
        return nums
    
test = Solution()
nums = [1]
print(test.exchange(nums))