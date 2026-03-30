# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        curr = head
        lead = head.next
        while lead and lead.next:
            if curr.val == lead.val:
                return True
            else:
                curr = curr.next
                lead = lead.next.next
        
        return False


        