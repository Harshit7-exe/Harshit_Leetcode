# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy_node = ListNode(0, head)
        i = j = dummy_node
        for _ in range(n +1):   #i is moving n + 1 terms because j will point to the node to be removed
            i = i.next
        while i:
            i = i.next
            j = j.next
        j.next = j.next.next
        return dummy_node.next
        
        