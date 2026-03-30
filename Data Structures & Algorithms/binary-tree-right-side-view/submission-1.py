# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack_t = [root]
        ans = [root.val]
        while stack_t:
            temp = []
            for node in stack_t:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right) 
            if temp:
                ans.append(temp[-1].val)
                stack_t = temp
            else:
                break
        return ans

            

        