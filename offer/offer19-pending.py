"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符
而'*'表示它前面的字符可以出现任意次（含0次）
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""

# 类似修改字符串的最少步数
# 初始条件：队首必须匹配
# 对于pat[j],seq[i]:
# 0.0 如果pat[j]，判断pat[j] == seq[i]，否则match[i,j] = false
# 0.1 match[i,j] = match[i-1, j-1] and match[i,j]
# 1.0 如果pat[j].，先判断pat[j] == seq[i]，满足转入1.1
# 1.1 
# 2.0 如果pat[j]*：如果pat[j] == seq[i]，当前位匹配则转入1.1，否则转入2.1
# 2.1 match[i,j] = match[i-1, j-1]

class Solution(object):
    def isMatch(self, seq: str, pat: str) -> bool:
        
