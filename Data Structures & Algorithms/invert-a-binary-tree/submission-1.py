# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp_left = root.left
        tmp_right = root.right
        root.right = self.invertTree(tmp_left)
        root.left = self.invertTree(tmp_right)
        return root
        