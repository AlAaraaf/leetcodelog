class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createListNode(seq):
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    node = head
    for i in range(1,len(seq)):
        node.next = ListNode(seq[i])
        node = node.next
    return head

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTreeNodeByLayerSeq(seq:list) -> TreeNode:
    if seq == []:
        return None
    
    ListSeq = len(seq)
    seqIdx = 0
    queue = [TreeNode(seq[0])]
    head = queue[0]
    while seqIdx < ListSeq:
        currentNode = queue.pop()
        if (seqIdx + 1 < ListSeq) and seq[seqIdx + 1] != "null":
            currentNode.left = TreeNode(seq[seqIdx + 1])
            queue.insert(0,currentNode.left)
        else:
            currentNode.left = None

        if (seqIdx + 2 < ListSeq) and seq[seqIdx + 2] != "null":
            currentNode.right = TreeNode(seq[seqIdx + 2])
            queue.insert(0,currentNode.right)
        else:
            currentNode.right = None
        seqIdx = seqIdx + 2
    
    return head