# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        while prev:
            tempH,tempP = head.next, prev.next
            head.next = prev
            prev.next = tempH
            head = tempH
            prev = tempP
        return None
        
            

