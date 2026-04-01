# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = deque([p])
        stack_q = deque([q])
        while stack_p and stack_q:
            for _ in range(len(stack_p)):
                
                curr_p = stack_p.popleft()
                curr_q = stack_q.popleft()
                if not curr_p and not curr_q:
                    continue
                if not curr_p or not curr_q:
                    return False
                if curr_p.val != curr_q.val:
                    return False
                
                stack_p.append(curr_p.left) 
                stack_p.append(curr_p.right)            
                stack_q.append(curr_q.left)             
                stack_q.append(curr_q.right) 
        
        return True

        