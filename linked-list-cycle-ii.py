# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) Time | O(1) Space, where n is number of nodes in list
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return
        slow = head.next
        fast = head.next.next

        while fast is not None and fast.next is not None and slow != fast:
            slow = slow.next
            fast = fast.next.next
        
        if fast is None or fast.next is None:
            return
        
        slowTwo = head
        while slowTwo != slow:
            slowTwo = slowTwo.next
            slow = slow.next
        return slow
