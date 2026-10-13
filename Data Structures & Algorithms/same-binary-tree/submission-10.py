# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checking(p, q):
            if p == None and q == None:
                return True
            if (p == None and q) or (p and q == None):
                return False
            if p.val == q.val:
                return checking(p.right, q.right) and checking(p.left, q.left)           
            else:
                return False
        if p == None and q == None:
            return True
        
        return checking(p, q)    