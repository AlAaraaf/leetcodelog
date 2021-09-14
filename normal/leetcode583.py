"""
给定两个单词word1和word2，找到使得word1和word2相同所需的最小步数
每步可以删除任意一个字符串中的一个字符

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 边界条件
        w1_len = len(word1)
        w2_len = len(word2)
        if w1_len == 0 or w2_len == 0:
            return max(w1_len, w2_len)
        
        # 转移状态记录MinSteps[i,j] - 使得w1[0:i]与w2[0:j]相同所需要的最小步数
        MinSteps = []
        for i in range(0, w1_len + 1):
            new_list = [0] * (w2_len + 1)
            MinSteps.append(new_list)
        
        # 初始条件
        for i in range(0, w1_len + 1):
            MinSteps[i][0] = i
        for j in range(0, w2_len + 1):
            MinSteps[0][j] = j
        
        for i in range(0, w1_len):
            for j in range(0, w2_len):
                w1_idx = i + 1
                w2_idx = j + 1
                if word1[i] == word2[j]:
                    MinSteps[w1_idx][w2_idx] = MinSteps[w1_idx - 1][w2_idx - 1]
                else:
                    Delete1 = MinSteps[w1_idx - 1][w2_idx] + 1
                    Delete2 = MinSteps[w1_idx][w2_idx - 1] + 1
                    DeleteBoth = MinSteps[w1_idx - 1][w2_idx - 1] + 2
                    MinSteps[w1_idx][w2_idx] = min(Delete1, Delete2, DeleteBoth)
        
        return MinSteps[w1_len][w2_len]

test = Solution()
word1 = "sea"
word2 = "eat"
print(test.minDistance(word1, word2))