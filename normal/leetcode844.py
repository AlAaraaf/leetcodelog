"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 #代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”

提交1 - 超时 (GoBack边界规则错误)
提交2,3 - 解答错误
主要的问题是退格的规则没有搞清楚&没有抽象清楚|边界判定条件不清楚（写注释啊
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # core: 从最后一位向前比较
        s_len = len(s)
        t_len = len(t)

        # 进行比较的位置
        s_comp = self.GoBack(s,s_len - 1)
        t_comp = self.GoBack(t,t_len - 1)

        while s_comp >= 0 and t_comp >= 0:
            
            # 当前位置比较
            print("s[{0}]:{1}".format(s_comp,s[s_comp]))
            print("t[{0}]:{1}".format(t_comp,t[t_comp]))
            if s[s_comp] != t[t_comp]:
                return False
            
            # 退格判定
            if s_comp >= 0 and t_comp >= 0:
                s_comp = self.GoBack(s,s_comp - 1)
                t_comp = self.GoBack(t,t_comp - 1)
            else:
                break
        
        if s_comp < 0 and t_comp < 0:
            return True
        else:
            return False
    
    def GoBack(self, arr, loc):
        back = 0
        while loc >=0 and (back != 0 or arr[loc] == "#"):
            if arr[loc] == "#": # 当前位置为退格号，继续往前看，退格数量增加
                loc -= 1
                back += 1
            else:
                loc -= 1 # 退格数量未清零，需要删除当前元素
                back -= 1
        print("after backspace: {0}[{1}]:{2}".format(arr, loc, arr[loc]))
        return loc
    

test = Solution()
s = "bxj##tw"
t = "bxj###tw"
print(test.backspaceCompare(s,t))