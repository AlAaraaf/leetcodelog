"""
请实现一个函数按照之字形顺序打印二叉树:
即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

广度优先打印正常层次顺序的二叉树
按照下标拆分成多个数列并进行倒序处理
"""

import math
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
        
        def BFSBinaryTree(root: TreeNode):
            queue = [root]
            outputSeq = []

            while queue != []:
                currentNode = queue.pop()
                if currentNode == None:
                    outputSeq.append("null") #  includes empty nodes in sequence for correctly calculation
                else:    
                    outputSeq.append(currentNode.val)
                    queue.insert(0, currentNode.left)
                    queue.insert(0, currentNode.right)
            return outputSeq

        layerSeq = BFSBinaryTree(root)
        # print(layerSeq)
        outputSeq = []
        SeqLen = len(layerSeq)
        LayerNum = math.ceil(math.log(SeqLen + 1,2))
        seqIdx = 0
        for i in range(LayerNum):
            currentLayer = []
            while seqIdx < SeqLen and seqIdx+1 <= (int(math.pow(2,i+1)) - 1):
                # print(layerSeq[seqIdx], seqIdx + 1, i+1, math.pow(2, i + 1) - 1)
                if i % 2 == 0 and layerSeq[seqIdx] != "null":
                    currentLayer.append(layerSeq[seqIdx])
                elif layerSeq[seqIdx] != "null":
                    currentLayer.insert(0, layerSeq[seqIdx])
                seqIdx += 1
            
            if currentLayer != []:
                outputSeq.append(currentLayer)
        
        return outputSeq

test = Solution()
seq = [1,2,"null",3,"null",4,"null",5]
head = createTreeNodeByLayerSeq(seq)
print(test.levelOrder(head))