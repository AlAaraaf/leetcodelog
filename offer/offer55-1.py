"""
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
"""

from util import createTreeNodeByLayerSeq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        ldepth = self.maxDepth(root.left) if root.left != None else 0
        rdepth = self.maxDepth(root.right) if root.right != None else 0
        
        return max(ldepth, rdepth) + 1

test = Solution()
tree = [3]
root = createTreeNodeByLayerSeq(tree)
print(test.maxDepth(root))