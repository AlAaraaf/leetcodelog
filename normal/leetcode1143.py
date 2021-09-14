"""
给定两个字符串text1和text2，返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列 ，返回0
一个字符串的子序列是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为3

输入：text1 = "abc", text2 = "abc"
输出：3

输入：text1 = "abc", text2 = "def"
输出：0
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 边界条件
        t1_len = len(text1)
        t2_len = len(text2)
        if t1_len == 1 or t2_len == 1:
            if t1_len == 1:
                return 1 if text1 in text2 else 0
            return 1 if text2 in text1 else 0

        # 转移状态记录 - MaxLength[i,j] - text1[0:i]与text2[0:j]的最长公共子序列长度
        MaxLength = []
        for i in range(0, t1_len + 1):
            new_list = [0] * (t2_len + 1)
            MaxLength.append(new_list)
        
        for i in range(0, t1_len):
            for j in range(0, t2_len):
                t1_idx = i + 1
                t2_idx = j + 1
                if text1[i] == text2[j]:
                    MaxLength[t1_idx][t2_idx] = MaxLength[t1_idx - 1][t2_idx - 1] + 1
                else:
                    NotInclude1 = MaxLength[t1_idx - 1][t2_idx]
                    NotInclude2 = MaxLength[t1_idx][t2_idx - 1]
                    NotIncludeBoth = MaxLength[t1_idx - 1][t2_idx - 1]
                    MaxLength[t1_idx][t2_idx] = max(NotInclude1, NotInclude2, NotIncludeBoth)
        
        return MaxLength[t1_len][t2_len]

test = Solution()
text1 = "abc"
text2 = "def"
print(test.longestCommonSubsequence(text1, text2))