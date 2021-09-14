"""
给定两个由一些闭区间组成的列表，firstList和secondList
其中firstList[i] = [starti, endi]
secondList[j] = [startj, endj]
每个区间列表都是成对不相交的，并且已经排序

返回这两个区间列表的交集
两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]

输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]

输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]

输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

提交1 - 解答错误 {[[14,16]]|[[7,13],[16,20]]} 判断条件写成了loc2 + 1 < len_first
提交2 - 解答错误 {[[4,11]]|[[1,2],[8,11],[12,13],[14,15],[17,19]] -> [[8,11],[12,11],[14,11],[17,11]]} 移动终止条件不全
"""

class Solution:
    def intervalIntersection(self, firstList: list, secondList: list) -> list:
        # 边界维护
        len_first = len(firstList)
        len_second = len(secondList)
        # 一方为空集，无重叠区域
        if len_first == 0 or len_second == 0: 
            return []
        # 边界判断无重叠区域
        if firstList[0][0] > secondList[-1][1] or firstList[-1][1] < secondList[0][0]:
            return []
        
        result = []
        last_chunk = [-1,-1]
        loc1 = 0
        loc2 = 0

        while loc1 < len_first and loc2 < len_second:
            # print("l1：{0}， l2:{1}".format(firstList[loc1],secondList[loc2]))
            # 当前的l1在l2左侧，l1向右移
            if firstList[loc1][1] < secondList[loc2][0]:
                if loc1 + 1 < len_first:
                    # print("move l1")
                    loc1 += 1
                    continue
                else:
                    break
            
            # 当前的l1在l2右侧，l2向右移
            if firstList[loc1][0] > secondList[loc2][1]:
                if loc2 + 1 < len_second:
                    # print("move l2")
                    loc2 += 1
                    continue
                else:
                    break
            
            # 当前l1,l2有重叠
            counter_start = max(firstList[loc1][0], secondList[loc2][0])
            counter_end = min(firstList[loc1][1], secondList[loc2][1])
            # print("counter: ",[counter_start, counter_end])
            
            # 修改交集列表
            # 1 上一交集的终点小于当前交集的起点，添加新的交集
            if last_chunk[1] < counter_start:
                result.append([counter_start, counter_end])
                last_chunk = [counter_start, counter_end]
            # 2 上一交集的终点大于或等于当前交集的起点且小于当前交集的终点，修改上一交集的终点
            elif last_chunk[1] >= counter_start and last_chunk[1] < counter_end:
                result[-1][1] = counter_end
            
            # 区间终点靠左的队列指针向右移或终止查找
            if loc1 + 1 == len_first and loc2 + 1 == len_second:
                break
            if counter_end == firstList[loc1][1] and loc1 + 1 < len_first:
                loc1 += 1
            else:
                loc2 += 1

        return result

test = Solution()
first = [[4,11]]
second = [[1,2],[8,11],[12,13],[14,15],[17,19]]
print(test.intervalIntersection(first, second))
