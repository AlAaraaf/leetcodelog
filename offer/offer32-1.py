"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if root == None:
            return []
        queue = [root]
        outputList = []
        while len(queue) > 0:
            node = queue[0]
            outputList.append(node.val)
            del queue[0]
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return outputList