# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checking(root, lower, upper):
            if root == None:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            return checking(root.right, root.val, upper) and checking(root.left, lower, root.val)
        
        return checking(root, float('-inf'), float('inf'))
            
        