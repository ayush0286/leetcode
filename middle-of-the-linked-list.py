# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Time | O(1) Space, where n is length of linked list
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast is not None:
            if fast.next is None:
                return slow
            if fast.next.next is None:
                fast = fast.next
            else:
                fast = fast.next.next
            slow = slow.next
        
