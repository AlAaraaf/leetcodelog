"""
已知一个长度为n的数组，预先按照升序排列，经由1到n次旋转后，得到输入数组。
例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次的结果为:
[a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值互不相同的数组nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。
请你找出并返回数组中的最小元素。

输入：nums = [3,4,5,1,2]
输出：1
输入：nums = [4,5,6,7,0,1,2]
输出：0
输入：nums = [11,13,15,17]
输出：11
"""
class Solution:
    def findMin(self, nums: list) -> int:
        # 二分查找旋转分界 -> 查找比s0高的峰值
        start_idx = 0
        end_idx = len(nums) - 1
        sequence_length = end_idx + 1
        mid = int((start_idx + end_idx) / 2)

        while (start_idx < end_idx):
            # print("enter peak search")
            # 中点与s0相同，或区间长度为1，直接比较start与end大小
            if mid == 0 or end_idx - start_idx == 1:
                if (nums[start_idx] > nums[end_idx]):
                    mid = start_idx
                    break
                else:
                    mid = end_idx
                    break
            # 中点比s0低，峰值在左侧，不需保留中点
            if nums[mid] < nums[0]:
                end_idx = mid - 1
                mid = int((start_idx + end_idx) / 2)
                # print("peak search: {0},{1},{2}".format(start_idx,mid,end_idx))

            # 中点比s0高，峰值在右侧，需保留中点 (作为peak candidate)
            if nums[mid] > nums[0]:
                start_idx = mid
                mid = int((start_idx + end_idx) / 2) 
                # print("peak search: {0},{1},{2}".format(start_idx, mid, end_idx))
        
        # print("peak search result, mid = ",mid)
        if (mid + 1 < sequence_length):
            return nums[mid + 1] # 峰值右侧仍有元素，则峰值右侧元素为最小值
        else:
            return nums[0] # 峰值右侧无值，则最小值在队首

solution = Solution()
nums = [1,0]
print(solution.findMin(nums))