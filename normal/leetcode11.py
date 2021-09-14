"""
给你 n 个非负整数 a1，a2，...，an每个数代表坐标中的一个点 (i, ai)
在坐标内画n条垂直线，垂直线i的两个端点分别为 (i, ai) 和 (i, 0)
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 使得abs(i-j)*min(ai,aj)最大

输入：[1,8,6,2,5,4,8,3,7]
输出：49 

输入：height = [1,1]
输出：1

输入：height = [4,3,2,1,4]
输出：16

输入：height = [1,2,1]
输出：2

提交1：解答错误 - {[2,3,4,5,18,17,6] - 17}， 转移条件错误
"""

class Solution:
    def maxArea(self, height: list) -> int:
        # （以高换宽）从容器两端向中间寻找边界
        length = len(height)
        MaxVol = (length - 1) * min(height[0], height[length - 1])

        start_idx = 0
        end_idx = length - 1

        # 每次移动较短的边
        while start_idx < end_idx:
            LeftValue = height[start_idx]
            RightValue = height[end_idx]
            if LeftValue > RightValue: # move right
                end_idx -= 1
            else: # move left
                start_idx += 1
            CurrentVol = (end_idx - start_idx) * min(height[end_idx], height[start_idx])
            if CurrentVol > MaxVol:
                MaxVol = CurrentVol
        
        return MaxVol

test = Solution()
height = [2,3,4,5,18,17,6]
print(test.maxArea(height))