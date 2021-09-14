"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
输入：s = "We are happy."
输出："We%20are%20happy."

0 <= s 的长度 <= 10000
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ','%20')

test = Solution()
strs = "We are happy."
print(test.replaceSpace(strs))