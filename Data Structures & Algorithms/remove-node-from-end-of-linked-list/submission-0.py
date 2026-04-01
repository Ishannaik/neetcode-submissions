# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        dummy = ListNode(0)
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        print(lst)
        lst.pop(len(lst) - n)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next