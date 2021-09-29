"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

输入：nums = [3,4,3,3]
输出：4
输入：nums = [9,1,7,9,7,9,7]
输出：1

1 <= nums.length <= 10000
1 <= nums[i] < 2^31
"""
class Solution:
    def singleNumber(self, nums: list) -> int:
        hashMap = dict()
        
        for number in nums:
            if number in hashMap.keys():
                if hashMap[number] == 2:
                    hashMap.pop(number)
                else:
                    hashMap[number] += 1
            else:
                hashMap[number] = 1
        
        return hashMap.popitem()[0]

test = Solution()
nums = [1,1,1,3,4,4,4]
print(test.singleNumber(nums))