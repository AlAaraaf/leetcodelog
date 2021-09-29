"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

输入: [10,2]
输出: "102"
输入: [3,30,34,5,9]
输出: "3033459"

0 < nums.length <= 100
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

自定义排序规则
"""

import functools

class Solution:
    def minNumber(self, nums: list) -> str:
        def ComparePrinciple(x,y) -> int:
            strA = int("".join([x, y]))
            strB = int("".join([y, x]))
            if strA > strB:
                return 1
            elif strA < strB:
                return -1
            return 0
        
        nums = [str(x) for x in nums]
        nums.sort(key=functools.cmp_to_key(ComparePrinciple))
        Res = "".join(nums)
        return Res

test = Solution()
nums = [0,10,2]

print(test.minNumber(nums))