# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.val == key:
            if root.left == None and root.right == None:
                return None
        
            elif root.left and root.right:
                aux = root.right
                while aux.left != None:
                    aux = aux.left
                
                root.val = aux.val
                root.right = self.deleteNode(root.right, aux.val)
                return root
            
            elif root.right:
                return root.right
            else:
                return root.left
        
        else:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
            return root
