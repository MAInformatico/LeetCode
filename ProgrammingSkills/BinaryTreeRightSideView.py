# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:                        
        def exploreTree(current,depth,currentDepth):            
            if not current:
                return depth
            
            if currentDepth > depth:
                result.append(current.val)
                depth = currentDepth
            depth = exploreTree(current.right, depth, currentDepth + 1)
            depth = exploreTree(current.left, depth, currentDepth + 1)
            return depth
            
            
        result = []
        exploreTree(root,0,1)
        return result
