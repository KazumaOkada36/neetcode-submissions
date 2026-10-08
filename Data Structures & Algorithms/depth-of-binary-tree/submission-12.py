# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxy = 0
        def track_count(count, root):
            maxy = count
            if root.right:
                maxy = max(track_count(count+1, root.right), maxy)
            if root.left:
                maxy = max(maxy, track_count(count+1, root.left))
            
            return maxy
        
        if root:
            return track_count(1, root)
        else:
            return 0

        