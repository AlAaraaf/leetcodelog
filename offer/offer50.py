"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        
        if s == '':
            return ' '

        char_index = {}
        for char in s:
            char_index[char] = char_index.get(char, 0) + 1
        
        for char in s:
            if char_index[char] == 1:
                return char
        
        return " "

test = Solution()
s = 'abaccdeff'
print(test.firstUniqChar(s))