# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_head = ListNode()
        i = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                i.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                i.next = list2
                list2 = list2.next
            i = i.next
        if list1:
            i.next = list1
        else:
            i.next = list2
        return new_head.next
