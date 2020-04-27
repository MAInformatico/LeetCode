# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lresult = []
        if not root: return lresult
        
        auxqueue = []
        auxqueue.append(root)
        
        while auxqueue:
            temp = []
            length = len(auxqueue)
            for i in range(length):
                node = auxqueue.pop(0)
                temp.append(node.val)
                
                if node.left:
                    auxqueue.append(node.left)
                if node.right:
                    auxqueue.append(node.right)
            lresult.append(temp)
        return lresult
