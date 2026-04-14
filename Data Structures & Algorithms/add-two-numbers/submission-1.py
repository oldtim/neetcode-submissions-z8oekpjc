# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        tmp_ans = ans
        residue = 0
        while l1 or l2:
            if l1 and l2:
                next_ans = ListNode()
                tmp_ans.next = next_ans
                tmp_ans = next_ans
                tmp_ans.val = (l1.val + l2.val + residue)%10
                residue = (l1.val + l2.val + residue)//10
                l1 = l1.next
                l2 = l2.next
                
            elif not l1 and l2:
                next_ans = ListNode()
                tmp_ans.next = next_ans
                tmp_ans = next_ans
                tmp_ans.val = (l2.val + residue)%10
                residue = (l2.val + residue)//10
                l2 = l2.next
                
            else:
                next_ans = ListNode()
                tmp_ans.next = next_ans
                tmp_ans = next_ans
                tmp_ans.val = (l1.val + residue)%10
                residue = (l1.val + residue)//10
                l1 = l1.next
                
        if residue != 0:
            next_ans = ListNode()
            tmp_ans.next = next_ans
            tmp_ans = next_ans
            tmp_ans.val = residue
            tmp_ans.next = None
        else:
            tmp_ans.next = None
            
        return ans.next




            




        