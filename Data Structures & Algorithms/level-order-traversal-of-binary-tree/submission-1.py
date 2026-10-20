# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        listy = []
        if root == None:
            return listy
        queue = [root]
        while queue:
            bruh = []
            level = len(queue)
            for i in range(level):                
                damn = queue.pop(0)
                bruh.append(damn.val)
                if damn.left:
                    queue.append(damn.left)
                if damn.right:
                    queue.append(damn.right)
            listy.append(bruh)
        return listy
            
        