"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
0 <= num < 2^31

动态规划
注意诸如“00”的字符串不是一个能够翻译的数字
"""

class Solution:
    def translateNum(self, num: int) -> int:
        
        if num <= 9:
            return 1

        num = str(num)
        numLen = len(num)
        firstNCount = [0] * numLen

        cmpValue = int("".join([num[0],num[1]]))
        firstNCount[0] = 1
        firstNCount[1] = 1 if cmpValue > 25 or cmpValue < 10 else 2
        for i in range(2,numLen):
            cmpValue = int("".join([num[i - 1],num[i]]))
            if cmpValue <= 25 and cmpValue >= 10:
                firstNCount[i] = firstNCount[i - 1] + firstNCount[i - 2]
            else:
                firstNCount[i] = firstNCount[i - 1]
        
        return firstNCount[numLen - 1]

test = Solution()
num = 100
print(test.translateNum(num))