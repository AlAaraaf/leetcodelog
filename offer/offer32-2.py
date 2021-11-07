"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""
from util import createTreeNodeByLayerSeq

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
        
        res = []
        queue = [root]
        
        while queue != []:
            nextQueue = []
            currentLayer = []
            while queue != []:
                currentNode = queue.pop()
                currentLayer.append(currentNode.val)
                if currentNode.left != None:
                    nextQueue.insert(0, currentNode.left)
                if currentNode.right != None:
                    nextQueue.insert(0, currentNode.right)
            queue = nextQueue
            res.append(currentLayer)

        return res

test = Solution()
tree = [3,9,20,"null","null",15,7]
root = createTreeNodeByLayerSeq(tree)
print(test.levelOrder(root))