# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_array = []

        def put_num_in_array(node):
            if node is None:
                return
            num_array.append(node.val)
            put_num_in_array(node.left)
            put_num_in_array(node.right)

        put_num_in_array(root)
        
        return sorted(num_array)[k - 1]