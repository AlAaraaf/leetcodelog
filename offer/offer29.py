"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""

class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if len(matrix) == 0:
            return []

        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        outputRes = []
        matLength = len(matrix)
        matWidth = len(matrix[0])
        totalCount = matLength * matWidth
        resCount = 0

        currentDir = 0
        xidx = 0
        yidx = 0

        currentX = [0, matLength - 1]
        currentY = [0, matWidth - 1]

        while resCount < totalCount:
            while currentX[0] <= xidx <= currentX[1] and currentY[0] <= yidx <= currentY[1]:
                outputRes.append(matrix[xidx][yidx])
                resCount += 1
                xidx += direction[currentDir][0]
                yidx += direction[currentDir][1]
            xidx = currentX[1] if xidx > currentX[1] else currentX[0] if xidx < currentX[0] else xidx
            yidx = currentY[1] if yidx > currentY[1] else currentY[0] if yidx < currentY[0] else yidx
            if direction[currentDir][0] > 0:
                currentY[1] -= 1
            elif direction[currentDir][0] < 0:
                currentY[0] += 1
            if direction[currentDir][1] > 0:
                currentX[0] += 1
            elif direction[currentDir][1] < 0:
                currentX[1] -= 1
            
            currentDir = currentDir + 1 if currentDir < 3 else 0
            xidx += direction[currentDir][0]
            yidx += direction[currentDir][1]
        
        return outputRes

test = Solution()
matrix = []
print(test.spiralOrder(matrix))