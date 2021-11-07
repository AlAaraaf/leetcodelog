"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
"""
from util import createTreeNodeByLayerSeq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        check each layer's left and right nodes at the same time
        """
        if root == None:
            return True

        def checkSymmetric(leftNode: TreeNode, rightNode: TreeNode):
            if leftNode == None and rightNode == None:
                return True
            elif (leftNode != None) ^ (rightNode != None):
                return False
            elif leftNode.val != rightNode.val:
                    return False
            else:
                lres = checkSymmetric(leftNode.left, rightNode.right)
                rres = checkSymmetric(leftNode.right, rightNode.left)
                return lres and rres

        
        return checkSymmetric(root.left, root.right)

test = Solution()
tree = [1,2,2,"null",3,3]
root = createTreeNodeByLayerSeq(tree)
print(test.isSymmetric(root))