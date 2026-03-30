"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_n = {None:None}
        curr = head
        while curr:
            hash_n[curr] = Node(curr.val)
            curr = curr.next
        #建立hash，使舊node(curr)，對應新node(Node(curr.val))
        
        curr2 = head
        while curr2:
            temp = hash_n[curr2]
            temp.next = hash_n[curr2.next]
            temp.random = hash_n[curr2.random]
            curr2 = curr2.next
        #再為新Node賦值，注意此時新Node.next和.random，是用hash_n來連結node
        return hash_n[head]
            


        