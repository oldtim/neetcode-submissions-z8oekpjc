# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lenth = 0
        count_head = head
        while count_head:
            lenth = lenth + 1
            count_head = count_head.next
        
        curr = head
        left_point = 1
        right_point = lenth
        while left_point + 1 < right_point:
            curr_right = curr
            for _ in range(right_point - left_point):
                curr_right = curr_right.next
            temp = curr.next
            curr.next = curr_right
            curr_right.next = temp
            curr = temp
            left_point = left_point + 1
            right_point = right_point - 1
        
        if left_point == right_point:
            curr.next = None
        if left_point + 1 == right_point:
            curr.next.next = None





        