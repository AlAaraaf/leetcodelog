"""
给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串
该字符串可以通过删除 s 中的某些字符得到
如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: list) -> str:
        dictionary.sort(key= lambda x : (-len(x), x))
        str_len = len(s)
        for pat in dictionary:
            node_in_pat = 0
            node_in_str = 0
            pat_len = len(pat)
            while node_in_pat < pat_len and node_in_str < str_len:
                if pat[node_in_pat] == s[node_in_str]:
                    node_in_pat += 1
                    node_in_str += 1
                else:
                    node_in_str += 1
            
            if node_in_pat == pat_len and node_in_str <= str_len:
                return pat

        return ""

test = Solution()
strs = "abpcplea"
dictionary = ["a","b","c"]
print(test.findLongestWord(strs, dictionary))