"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class GraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        cloned_node = GraphNode(node.val)
        cloned = {node:cloned_node}
        theList = [node]
        
        while theList:
            currentNode = theList.pop()
            for neighbor in currentNode.neighbors:
                if neighbor not in cloned:
                    theList.append(neighbor)
                    cloned_neighbor = GraphNode(neighbor.val)
                    cloned[neighbor] = cloned_neighbor
                cloned[currentNode].neighbors.append(cloned[neighbor])
        return cloned[node]
