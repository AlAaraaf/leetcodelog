"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
"""

# 假设当前数组为二叉搜索树的后序遍历
# 后序遍历的最后一位可用来拆分左右子树
# 左子树中没有比head大的，右子树中没有比head小的
# 分别判断左右子树是否也满足二叉搜索树条件

class Solution(object):
    def verifyPostorder(self, postorder: list) -> bool:
        # 边界条件判断
        current_length = len(postorder)
        if current_length <= 1:
            return True
        
        # 检验二叉搜索树条件
        head = postorder[-1]
        idx = 0
        while postorder[idx] < head: 
            idx += 1
        left_postorder = postorder[0:idx] # [0,idx] 为左子树
        right_postorder = postorder[idx:-1] # [idx,-1] 为右子树
        
        for item in right_postorder:
            if item < head:
                return False
        
        return self.verifyPostorder(left_postorder) and self.verifyPostorder(right_postorder)
