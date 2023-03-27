# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n + m) Time | O(1) Space, where n, and m are length of linked lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        nodeA = headA
        nodeB = headB
        if lengthA > lengthB:
            while lengthA - lengthB != 0:
                nodeA = nodeA.next
                lengthA -= 1
        elif lengthA < lengthB:
            while lengthB - lengthA != 0:
                nodeB = nodeB.next
                lengthB -= 1
        
        while nodeA is not None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
    

    def getLength(self, head):
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count