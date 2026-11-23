# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None # reference to the new linked list

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
