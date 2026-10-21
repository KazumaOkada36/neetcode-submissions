# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildy(l, r):
            nonlocal i
            if l>r:
                return None
            root = TreeNode(preorder[i])
            i+= 1
            index = inorder_map[root.val]

            root.left=buildy(l, index-1)
            root.right=buildy(index+1, r)

            return root

        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        i = 0

        return buildy(0, len(inorder)-1)
        



        

        