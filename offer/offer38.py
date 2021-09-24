"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

迭代 - 但是需要解决重复元素的问题
字典序 - 从头到尾按照字典序打印全排列结果
"""

class Solution:
    def permutation(self, s: str) -> list:
        if (len(s)) == 0:
            return []
        strList = []
        for i in range(len(s)):
            strList.append(s[i])
        strList.sort()
        allList = ["".join(strList)]

        def nextPermutation(currentList: list):
            listLen = len(currentList)
            swapPosition1 = 0
            swapPosition2 = 0
            i = listLen - 1
            while i >= 1:
                if currentList[i] > currentList[i-1]:
                    break
                i -= 1
            if i == 0:
                return [] # 没有下一个队列需要输出
            
            swapPosition1 = i-1
            j = i
            while j < listLen and currentList[j] > currentList[swapPosition1]:
                j += 1

            swapPosition2 = j - 1
            # print("before swap: {0},{1} - {2}".format(swapPosition1, swapPosition2, currentList))
            currentList[swapPosition1], currentList[swapPosition2] = currentList[swapPosition2], currentList[swapPosition1]
            # print("after swap: {0}".format(currentList))
            if swapPosition1 + 1 <= listLen - 1:
                # print("debugging:{1} - {0}".format(currentList[swapPosition1 + 1:], swapPosition1 + 1))
                reverseList = currentList[swapPosition1 + 1:]
                reverseList.reverse()
                currentList[swapPosition1 + 1:] = reverseList
            return currentList
        
        nextList = nextPermutation(strList)
        while nextList != []:
            allList.append("".join(nextList))
            nextList = nextPermutation(nextList)
        
        return allList

test = Solution()
strList = "1234"
print(test.permutation(strList))