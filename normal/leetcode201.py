"""
给你两个整数left和right，表示区间 [left, right]
返回此区间内所有数字，按“位与”的结果（包含 left 、right 端点）

输入：left = 5, right = 7
输出：4

输入：left = 0, right = 0
输出：0

输入：left = 1, right = 2147483647
输出：0

# 看了答案。。。（记得过几天重写一遍相关的题目）
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 边界确定
        if left == 0:
            return 0
        
        # 右移查找区间边界的公共前缀并记录移动数量
        offset = 0
        while left != right:
            left >>= 1
            right >>= 1
            offset += 1
        
        # 左移回退得到结果
        return left << offset