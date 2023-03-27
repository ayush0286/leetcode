# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) Time | O(1) Space, where n is length of remaining linked list
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
