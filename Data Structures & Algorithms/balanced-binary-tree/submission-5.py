# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            a = height(node.left)
            b = height(node.right)
            return 1+ max(a, b)
        k = root
        if k == None:
            return True
        a = height(k.right)
        b = height(k.left)
        if a<b-1 or b<a-1:
            return False
        return self.isBalanced(k.right) and self.isBalanced(k.left)

        