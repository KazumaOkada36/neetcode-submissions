# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        listy = []
        queue = [root]
        while queue:
            lengthy = len(queue)
            bruh = queue[0]
            listy.append(bruh.val)
            for i in range(lengthy):
                damn = queue.pop(0)
                if damn.right:
                    queue.append(damn.right)
                if damn.left:
                    queue.append(damn.left)



        return listy

            

        



        