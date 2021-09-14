"""
给你一个包含n个整数的数组nums，判断 nums 中是否存在三个元素a,b,c，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
输入：nums = []
输出：[]
输入：nums = [0]
输出：[]

执行1： 解答错误 ([0,0,0] -> []) 错误考虑边界条件（>0的情况才应该排除，而不是>=0)
执行2： 解答错误 ([-2,0,0,2,2] -> [[-2,0,2],[-2,0,2]]) 解决执行1的错误时没有举一反三想到左右指针所指元素也可能出现完全重复的情况
"""

from typing import Set


class Solution:
    def threeSum(self, nums: list) -> list:
        # 边界维护
        if len(nums) < 3:
            return []

        # 数组中不存在负数/0，不可能存在三元组
        SortedList = sorted(nums)
        if SortedList[0] > 0:
            return []

        # 从最小数开始使用左右指针查找
        Result = []
        ListLength = len(SortedList)
        a_idx = 0
        while ((a_idx < ListLength - 2) and SortedList[a_idx] <= 0):
            a = SortedList[a_idx]
            left_node = a_idx + 1
            right_node = ListLength - 1
            # print("start finding: a: {0}|{1}, leftnode: {2}, rightnode:{3}".format(a_idx, a,left_node,right_node))

            # 左右指针
            while (left_node < right_node):
                b = SortedList[left_node]
                c = SortedList[right_node]
                CurrentSum = a + b + c
                # print("iter: a - ({0},{1}), b - ({2},{3}), c - ({4},{5})".format(a_idx,a,left_node,b,right_node,c))
                if (CurrentSum == 0):
                    # 添加结果
                    Result.append([a,b,c])
                    # print("find one: {0}|{1}|{2}".format(a_idx, left_node, right_node))
                    # 移动指针，跳过相同大小元素
                    while (left_node < ListLength) and (SortedList[left_node] == b):
                        left_node += 1
                    while (right_node >= 0) and (SortedList[right_node] == c):
                        right_node -= 1
                    continue
                
                # 和比0小，移动左指针
                elif (CurrentSum < 0):
                    left_node += 1
                
                # 和比0大，移动右指针
                else:
                    right_node -= 1
            
            # 更新初始数所在位置
            while (a_idx + 1 < ListLength) and (SortedList[a_idx] == a):
                a_idx += 1
            # print("after update: a - {0}|{1}".format(a_idx, SortedList[a_idx]))

        return Result

solution = Solution()
nums = [-1]
print(solution.threeSum(nums))