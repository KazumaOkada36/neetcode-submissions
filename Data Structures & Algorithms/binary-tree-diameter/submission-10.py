# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxy = 0
        def new_func(root):
            nonlocal maxy
            g, l = 0, 0
            if root is None:
                return 0
            g = new_func(root.right)
            l = new_func(root.left)
            maxy=max(g+l, maxy)
            return 1+max(g, l)
        new_func(root)
        return maxy

        