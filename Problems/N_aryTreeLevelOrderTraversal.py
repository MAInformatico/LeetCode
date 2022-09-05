"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        levels = set()
        def DFS(node, level):
            if level not in levels:
                levels.add(level)
                result.append([])
            result[level].append(node.val)
            for i in node.children:
                DFS(i, level + 1)
                
        DFS(root,0)
        return result
