# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            left = dfs(node.left) if node.left else [0, 1]
            right = dfs(node.right) if node.right else [0, 1]
            if left[1] == 0 or right[1] == 0:
                sign = 0
            elif abs(left[0] - right[0]) > 1:
                sign = 0
            else:
                sign = 1
            return [max(left[0], right[0])+1, sign]
        
        ans = dfs(root)
        if ans[1] == 1:
            return True
        else:
            return False
        

        