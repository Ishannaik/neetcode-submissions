# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify the merge process
        tail = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If either list still has remaining elements, attach it to the end
        if list1:
            tail.next = list1
        else:  # This should be just else
            tail.next = list2

        # Return the merged list, starting after the dummy node
        return dummy.next
