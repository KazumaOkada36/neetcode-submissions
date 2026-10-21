# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        i = 0
        def buildy(l, r):
            nonlocal i

            if l > r:
                return None
            
            root = TreeNode(preorder[i])
            i += 1

            mid = inorder_map[root.val]

            root.left = buildy(l, mid-1)
            root.right = buildy(mid+1, r)

            return root

        return buildy(0, len(inorder)-1)

        



        

        