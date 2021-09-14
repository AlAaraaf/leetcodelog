"""
整数数组 nums 按升序排列，数组中的值互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转：
数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] （下标从0开始）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你旋转后的数组nums和一个整数target ，如果nums中存在这个目标值target ，则返回它的下标，否则返回 -1 。
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
输入：nums = [1], target = 0
输出：-1

执行1：超出时间限制 {[1,3],0} 峰值二分查找的边界维护和终止条件没有做好
执行2：解答错误 {[3,1],1} -> 应输出1，但输出0 第二个序列的二分查找结果在输出前没有经过整理
"""

class Solution:
    def search(self, nums: list, target: int) -> int:
        # 二分查找旋转分界（查找比s0高的峰值）
        start_idx = 0
        end_idx = len(nums) - 1
        sequence_length = end_idx + 1
        mid = int((start_idx + end_idx) / 2)

        while (start_idx < end_idx):
            # print("enter peak search")
            # 若在查找过程中碰到了target，则直接返回下标
            if nums[mid] == target:
                return mid
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

        # 双序列二分查找target
        # 边界维护
        if (mid + 1 < sequence_length):
            head_result = self.binary_search(nums[0 : mid + 1], target)
            tail_result = self.binary_search(nums[mid + 1 : sequence_length], target)
        else:
            head_result = self.binary_search(nums[0 : sequence_length], target)
            tail_result = -1

        if head_result != -1:
            return head_result
        elif tail_result != -1:
            return mid + 1 + tail_result
        else:
            return -1

    def binary_search(self, sequence, target):
        # 边界判断
        if len(sequence) == 0:
            return -1
        if sequence[0] > target or sequence[-1] < target:
            return -1
        
        # 二分查找
        start_idx = 0
        end_idx = len(sequence) - 1
        mid = int((start_idx + end_idx) / 2)

        while (start_idx < end_idx):
            if sequence[mid] == target:
                return mid
            
            if sequence[mid] < target:
                start_idx = mid + 1
                mid = int((start_idx + end_idx) / 2)
            
            if sequence[mid] > target:
                end_idx = mid - 1
                mid = int((start_idx + end_idx) / 2)
        
        if sequence[mid] != target:
            return -1
        
        return mid

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))