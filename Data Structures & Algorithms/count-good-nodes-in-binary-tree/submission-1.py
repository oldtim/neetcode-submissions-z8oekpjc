# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, max_val):
            if node.val >= max_val:
                nonlocal ans
                ans += 1
                max_val = node.val
            
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)

        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)
        return ans+1
        