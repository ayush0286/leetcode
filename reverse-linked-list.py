# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Time | O(1) Space, where n is length of linked list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None
        node = head
        while node is not None:
            newHead = node
            node = node.next
            newHead.next = reversedHead
            reversedHead = newHead
        return reversedHead
