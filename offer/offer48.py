"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

s.length <= 40000

动态规划 - maxSubString[i] = maxSubString[i-1] + 1 if NOT INCLUDE else 1
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCount = [0] * 256 # calculate each char's number in a substring
        maxLen = 0

        strLen = len(s)
        if strLen <= 1:
            return strLen

        maxSubString = [1] * strLen
        charCount[ord(s[0])] = 1

        for i in range(1,strLen):
            if charCount[ord(s[i])]:
                for j in range(maxSubString[i-1],0,-1):
                    if s[i-j] != s[i]:
                        charCount[ord(s[i-j])] = 0
                    else:
                        maxSubString[i] = j
                        break
            else:
                maxSubString[i] = maxSubString[i - 1] + 1
            charCount[ord(s[i])] = 1
            if maxSubString[i] > maxLen:
                maxLen = maxSubString[i]
        
        # print(maxSubString)
        return maxLen

test = Solution()
testStr = ' '
print(test.lengthOfLongestSubstring(testStr))