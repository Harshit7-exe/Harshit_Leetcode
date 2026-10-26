# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        def dfs(node, depth):
            if not node:
                return 
            if depth == len(result):
                result.append([])
            if depth % 2 == 0:
                result[depth].append(node.val)
            else:
                result[depth].insert(0, node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return result
        