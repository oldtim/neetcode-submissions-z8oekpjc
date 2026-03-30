# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        #因為迴圈是由list其中之一跑完而結束，所以其中之一list = None，只會連到剩下的list

        return dummy.next

        ##失敗。搞太複雜:看解答
        ##我的寫法太複雜，是因為我的思維太侷限在:藉由兩個pointer分別讀取兩條list，來修改兩條list之間的連結
        ##而solution精妙之處，在於用一個pointer去追蹤兩個list中的較小點
        # curr1 = list1
        # curr2 = list2
        # if not curr1:
        #     return curr2
        # if not curr2:
        #     return curr1
        # while curr1 and curr2:
        #     if curr1.val <= curr2.val:
        #         if curr1.next and curr1.next.val <= curr2.val:
        #             curr1 = curr1.next
        #         else:
        #             temp = curr1.next
        #             curr1.next = curr2
        #             curr1 = temp
                
        #     else:
        #         if curr2.next and curr2.next.val <= curr1.val:
        #             curr2 = curr2.next
        #         else:
        #             temp2 = curr2.next
        #             curr2.next = curr1
        #             curr2 = temp2
        # if list1.val <= list2.val:
        #     return list1
        # else:
        #     return list2


        