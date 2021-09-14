"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

输入：word1 = "intention", word2 = "execution"
输出：5
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 边界判断
        w1_len = len(word1)
        w2_len = len(word2)
        if w1_len == 0 or w2_len == 0:
            return max(w1_len, w2_len)
        
        # 转移状态记录：MinSteps[i,j] - 从w1[0:i]到w2[0:j]所用的最少操作数
        MinSteps = []
        for j in range(0, w1_len + 1):
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
                Replace = MinSteps[w1_idx - 1][w2_idx - 1]
                Insert = MinSteps[w1_idx][w2_idx - 1] + 1
                Delete = MinSteps[w1_idx - 1][w2_idx] + 1

                if word1[i] == word2[j]:
                    MinSteps[w1_idx][w2_idx] = min(Replace, Insert, Delete)
                else:
                    MinSteps[w1_idx][w2_idx] = min(Replace + 1, Insert, Delete)
                
                # print("Replace:{0}, Insert:{1}, Delete:{2}".format(Replace, Insert, Delete))
                # print("MinStep[{0},{1}] = {2}".format(i,j,MinSteps[i][j]))
        
        return MinSteps[w1_len][w2_len]
    
test = Solution()
word1 = "horse"
word2 = "ros"
print(test.minDistance(word1, word2))