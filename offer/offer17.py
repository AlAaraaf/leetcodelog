"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
"""

class Solution:
    def printNumbers(self, n: int) -> list:
        """
        basically considering BIG number that need to use string
        """
        
        self.ResList = []
        self.NumList = ['0' for item in range(n)]

        def generateNum(currentDigit: int):
            if currentDigit == n - 1:
                self.ResList.append(''.join(self.NumList).lstrip('0'))
                return
            for i in range(10):
                self.NumList[currentDigit + 1] = str(i)
                generateNum(currentDigit + 1)
        
        for i in range(10):
            self.NumList[0] = str(i)
            generateNum(0)

        self.ResList.remove('')
        listLen = len(self.ResList)
        for idx in range(listLen):
            self.ResList[idx] = int(self.ResList[idx])
        
        return self.ResList
    
test = Solution()
n = 4
print(test.printNumbers(n) == list(range(1, pow(10, n))))