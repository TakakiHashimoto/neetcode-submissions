# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            left_valid = validate(node.left, lower, node.val)
            right_valid = validate(node.right, node.val, upper)

            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf"))