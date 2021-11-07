"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""
from util import createTreeNodeByLayerSeq, printTreeByLayerSeq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        def mirrorCurrentNode(root: TreeNode):
            if root.left != None:
                root.left = mirrorCurrentNode(root.left)
            if root.right != None:
                root.right = mirrorCurrentNode(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        
        return mirrorCurrentNode(root)

test = Solution()
tree = [4,2,7,1,3,6,9]
root = createTreeNodeByLayerSeq([])
res = test.mirrorTree(root)
printTreeByLayerSeq(res)