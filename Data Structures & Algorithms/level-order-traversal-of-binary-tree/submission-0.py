# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        #用[root]是因為deque() 需要的是一個 iterable，而 root 是一個單一物件（TreeNode）
        ans = []

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
        



        