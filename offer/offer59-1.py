"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
"""

# 找到第一个滑动窗口的最大值及其位置
# 对于之后的滑动窗口，最大值为：
# 1. 上一窗口的最大值（有效的话）
# 2. 窗口滑动后的最大值（原最大值已无效）
# 但是比较的次数还是会很多，如果维护一个单调队列应该效率更高

class Solution(object):
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        # 边界条件判断
        listLength = len(nums)
        if listLength == 0:
            return []
        
        max = float("-Inf")
        max_idx = -1

        maxInChunk = []

        for i in range(0, len(nums) - k + 1):
            if max_idx >= i and max_idx < i + k:
                if max > nums[i + k - 1]:
                    maxInChunk.append(max)
                else:
                    max = nums[i + k - 1]
                    max_idx = i + k - 1
                    maxInChunk.append(max)
            else:
                max, max_idx = self.findMaxInChunk(nums[i : i + k])
                maxInChunk.append(max)
        
        return maxInChunk
    
    def findMaxInChunk(self, seq):
        max = float("-Inf")
        max_idx = -1
        for i in range(0, len(seq)):
            if seq[i] >= max:
                max = seq[i]
                max_idx = i
        
        return max, max_idx

test = Solution()
nums = [1,3,-1,2,-3,5,3,6,7]
k = 3
print(test.maxSlidingWindow(nums, k))
