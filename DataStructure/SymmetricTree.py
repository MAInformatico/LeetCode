# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        queue = deque()
        queue.append((root,root))

        while queue:
            
            for _ in range(len(queue)):
                childLeft, childRight = queue.popleft()
                
                
                if not childLeft and not childRight:
                    continue
                elif not childLeft or not childRight:
                    return False
                else:
                    if childLeft.val != childRight.val:
                        return False
                    else:
                        queue.append((childLeft.left, childRight.right))
                        queue.append((childLeft.right, childRight.left))

            return True        
