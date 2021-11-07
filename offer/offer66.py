"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
"""

class Solution:
    def constructArr(self, a: list) -> list:

        if a == []:
            return []

        res = []
        listLen = len(a)
        lres = [1 for item in range(listLen)]
        rres = [1 for item in range(listLen)]

        for i in range(1,listLen):
            lres[i] = a[i - 1] * lres[i - 1]
        
        for i in range(listLen - 2, -1, -1):
            rres[i] = a[i + 1] * rres[i + 1]
        
        for i in range(listLen):
            res.append(lres[i] * rres[i])
        
        return res

test = Solution()
a = [1,2,3,5,4]
print(test.constructArr(a))