# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Time | O(1) Space, where n is length of linked list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prior = head
        curr = head
        prev = None
        count = 1
        while count != n:
            prior = prior.next
            count += 1
        # if n from end is head of list
        if prior.next is None:
            curr = curr.next
            head.next = None
            head = curr
            return head
        
        while prior.next is not None:
            prior = prior.next
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None
        return head
