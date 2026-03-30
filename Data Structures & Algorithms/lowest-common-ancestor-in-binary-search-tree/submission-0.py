# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp_left = self.lowestCommonAncestor(root.left, p, q)
        tmp_right = self.lowestCommonAncestor(root.right, p, q)
        if root.val != p.val and root.val != q.val:
            if not tmp_left and not tmp_right:
                return None
            elif not tmp_left and tmp_right:
                return tmp_right
            elif not tmp_right and tmp_left:
                return tmp_left
            else:
                return root
        
        if root.val == p.val or root.val == q.val:
            return root



        