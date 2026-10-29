"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew={}
        def dfs(curr):
            if curr in oldtoNew:
                return oldtoNew[curr]
            newNode = Node(curr.val)
            oldtoNew[curr] = newNode
            newNode.val = curr.val
            newNode.neighbors=[]
            for neighbor in curr.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        
        if not node:
            return None
        return dfs(node)
        