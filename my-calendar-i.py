class MyCalendar:

    def __init__(self):
        self.calendar = None

    def book(self, start: int, end: int) -> bool:
        node = self.Node()
        node.value = [start, end]
        return self.addBooking(node)
        
    # O(n) Time | O(1) Space, where n is length of calendar 
    def addBooking(self, node):
        if self.calendar is None:
            self.calendar = node
            return True
        
        return self.validateBooking(node)
    
    def validateBooking(self, node):
        head = self.calendar
        start = node.value[0]
        end = node.value[1]
        if end <= head.value[0]:
            node.next = head
            head.prev = node
            self.calendar = node
            return True
        while head is not None:
            currStart = head.value[0]
            currEnd = head.value[1]
            if currEnd <= start:
                # insert here
                nextNode = head.next
                if nextNode is None:
                    head.next = node
                    node.prev = head
                    return True
                else:
                    if end <= nextNode.value[0]:
                        node.next = head.next 
                        node.prev = head
                        head.next = node
                        node.next.prev = node
                        return True
            head = head.next
        return False


    class Node:

        def __init__(self):
            self.value = None
            self.next = None
            self.prev = None


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
