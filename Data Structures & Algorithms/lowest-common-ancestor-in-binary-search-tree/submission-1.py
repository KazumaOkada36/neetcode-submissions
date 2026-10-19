# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_node(root, p, q):
            if p.val < root.val and q.val < root.val:
                return find_node(root.left, p, q)           
            elif p.val > root.val and q.val > root.val:
                return find_node(root.right, p, q)
            else:
                return root
        
        return find_node(root, p, q)