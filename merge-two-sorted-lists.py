# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n + m) Time | O(1) Space, where n and m are lengths of linked lists 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        headState = head
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
                head = head.next
            else:
                head.next = list1
                list1 = list1.next
                head = head.next
        
        if list1 is None:
            head.next = list2
        else:
            head.next = list1
        return headState
        
