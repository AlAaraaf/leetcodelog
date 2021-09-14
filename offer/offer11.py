"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

输入：[3,4,5,1,2]
输出：1
输入：[2,2,2,0,1]
输出：0

逐位比较直到出现违反递增的情况
"""
class Solution:
    def minArray(self, numbers: list) -> int:
        seq_len = len(numbers)
        i = 0
        while i + 1 < seq_len:
            if numbers[i] <= numbers[i + 1]:
                i += 1
            else:
                return numbers[i + 1]
        return numbers[0]

test = Solution()
numbers = [0,1,2,3,4,5]
print(test.minArray(numbers))