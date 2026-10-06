# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stop the recursion if no nodes are connected
        if root == None:
            return
        current = root
        left = current.left
        right = current.right
        root.left = right
        root.right = left
        self.invertTree(left)
        self.invertTree(right)

        return root