"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出

A B C E
S F C S
A D E E

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

dfs - 依旧有点慢（尝试建立邻接点图然后查找路径）
"""
class Solution:
    def exist(self, board: list, word: str) -> bool:
        width = len(board[0])
        length = len(board)
        textLen = len(word)
        visited = [[0 for x in range(width)] for y in range(length)]
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def DeepForwardSearch(x,y,textIdx):
            # out of range
            if textIdx >= textLen or x not in range(length) or y not in range(width):
                return False
            # chopping
            if visited[x][y] or board[x][y] != word[textIdx]:
                return False
            # termination
            if textIdx + 1 == textLen:
                return True
            
            visited[x][y] = 1
            # print(visited)
            subfixFound = False
            for dir in direction:
                subfixFound = subfixFound or DeepForwardSearch(x+dir[0],y+dir[1], textIdx + 1)
            visited[x][y] = 0
            return subfixFound

        # find the beginer of DFS
        for x in range(length):
            for y in range(width):
                if DeepForwardSearch(x,y,0):
                    return True
        return False

test = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ESEEDA"
print(test.exist(board, word))