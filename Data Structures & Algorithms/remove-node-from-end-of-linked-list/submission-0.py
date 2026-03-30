class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        count = length - n
        #錯誤寫法:prev = ListNode(0,head)
        #如果不另外設dummy，因prev會跑走，return會有麻煩
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(count):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next