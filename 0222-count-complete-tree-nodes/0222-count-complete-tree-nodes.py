# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def height(node):
            h = 0

            while node:
                h += 1
                node = node.left

            return h

        left_height = height(root.left)
        right_height = height(root.right)

        if left_height == right_height:
           
            return (2 ** left_height) + self.countNodes(root.right)

        else:
            
            return (2 ** right_height) + self.countNodes(root.left)