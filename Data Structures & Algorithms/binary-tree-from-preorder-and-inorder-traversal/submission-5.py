# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         def constructTree(preorder, inorder):
#             if not preorder:
#                 return None
#             root = TreeNode(preorder[0])
#             root_index = inorder.index(root.val)
#             left_size = root_index

#             left_inorder = inorder[:root_index]
#             right_inorder = inorder[root_index + 1:]

#             left_preorder = preorder[1:1 + left_size]
#             right_preorder = preorder[1 + left_size:]

#             root.left = constructTree(left_preorder, left_inorder)
#             root.right = constructTree(right_preorder, right_inorder)

#             return root

#         return constructTree(preorder, inorder)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        positions = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0

        def constructTree(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            root_index = positions[root_value]

            root.left = constructTree(left, root_index - 1)
            root.right = constructTree(root_index + 1, right)

            return root

        return constructTree(0, len(inorder) - 1)