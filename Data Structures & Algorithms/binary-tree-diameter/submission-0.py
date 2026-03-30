# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def __init__(self):
    #     self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]


        ## 以下我的code會卡住，1.是腦中想著一次將node的left和right排進stack，但正解中是先把所有left排進stack、由底部回溯後node值存入mp、然後再right
        ##                   2.用mp這個dict來取代global variable的功能，儲存每個node的height和diameter兩個值
        ##                   3. 正解用stack[-1]來讀取node，直到left和right的值都存入mp之後，才pop，也就是處理完成
        ##                   4. mp內一開始就存入None值的狀況
        # count_stack = [[root, 0]]
        # while count_stack:
        #     temp = coun_stack.pop()
        #     if temp[0].right:
        #         count_stack.append([temp[0].right, temp[1]+1])
        #     if temp[0].left:
        #         count_stack.append([temp[0].left, temp[1]+1])



        