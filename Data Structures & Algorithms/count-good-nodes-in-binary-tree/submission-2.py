# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def pleaseeeee_speed(root, maxy):
            county = 0
            if root == None:
                return county
            if root.val >= maxy:
                county += 1
                maxy = root.val
            a = pleaseeeee_speed(root.right, maxy)
            b = pleaseeeee_speed(root.left, maxy)
            return (a+b+county)

        return pleaseeeee_speed(root, root.val)

            
        