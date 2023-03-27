# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) Time | O(1) Space, where n is length of linked list
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        fast = head.next.next
        slow = head.next

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False