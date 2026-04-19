# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(curr1, curr2): 
            stack1 = deque([curr1])
            stack2 = deque([curr2])
            while stack2 and stack1:  #錯誤1.      
                mtree_node = stack1.popleft()
                subtree_node = stack2.popleft()
                if not mtree_node and not subtree_node:
                    continue
                if not mtree_node or not subtree_node:
                    return False
                if mtree_node.val != subtree_node.val:
                    return False
                stack1.append(mtree_node.left)
                stack1.append(mtree_node.right)
                stack2.append(subtree_node.left)
                stack2.append(subtree_node.right)
            return not stack1 and not stack2 #錯誤1.
        
        if not root:
            return False

        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        # else:
        #     if root.left:
        #         self.isSubtree(root.left, subRoot)
        #     if root.right:
        #         self.isSubtree(root.right, subRoot)


# 錯誤1. 沒考慮到其實題目並沒有規定mainTree一定大於subTree
#，因次function末回傳時判斷也要兩者同時不存在(stack用盡)才能回傳true
#                 


                       