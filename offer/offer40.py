"""
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""

class Solution:
    def getLeastNumbers_byHeap(self, arr: list, k: int) -> list:
        """
        使用堆在leetcode上超时了
        """
    
        listLen = len(arr)
        if k == 0 or listLen == 0:
            return []
        
        heap = arr[:k]

        def sortHeap():
            for pidx in range(k//2 - 1, -1, -1):
                cidx = pidx * 2 + 1
                while cidx < k:
                    if cidx + 1 < k and heap[cidx + 1] > heap[cidx]:
                        cidx += 1
                    if heap[pidx] < heap[cidx]:
                        temp = heap[pidx]
                        heap[pidx] = heap[cidx]
                        heap[cidx] = temp
                    pidx = cidx
                    cidx = cidx * 2 + 1
        
        # heap sort for topK minimum
        sortHeap()
        for i in range(k, listLen):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                sortHeap()
        
        return heap

    def getLeastNumbers(self, arr: list, k: int) -> list:
        
        if arr == [] or k == 0:
            return []

        arr.sort()
        return arr[:k]
        

test = Solution()
input = [0,0,1,2,4,2,2,3,1,4]
val = 8
print(test.getLeastNumbers(input, val))