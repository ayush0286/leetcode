# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(m + n) Time | O(1) Space, where n and m are lengths of linked lists
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        carry = 0
        while l1.next is not None and l2.next is not None:
            add = l1.val + l2.val + carry
            carry = add // 10
            node.val = add % 10
            node.next = ListNode()
            node = node.next
            l1 = l1.next
            l2 = l2.next
        add = l1.val + l2.val + carry
        carry = add // 10
        node.val = add % 10

        longer = None
        if l1.next is None:
            longer = l2
        else:
            longer = l1
        while longer.next is not None:
            longer = longer.next
            node.next = ListNode()
            node = node.next
            add = carry + longer.val
            node.val = add % 10
            carry = add // 10
        
        if carry != 0:
            node.next = ListNode()
            node = node.next
            node.val = carry
        
        return head
