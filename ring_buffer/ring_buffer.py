from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = DoublyLinkedList()
        self.current = None
        self.length = 0

    def append(self, item):
        if (self.length == self.capacity):  # check to see if length and capacity match
            if self.current.next is not None:  # if there is a next node
                self.current.value = item  # set the value to that node
                self.current = self.current.next  # move the pointer
            # if the next is none  (circle this to head)
            elif self.current.next is None:
                self.buffer.value = item  # set the value to the item
                self.current = self.buffer.head  # MUST CONNECT TAIL TO HEAD.
        else:
            self.buffer.add_to_tail(item)
            self.current = self.buffer.head
            self.length += 1

    def get(self):
        box = []  # make the box
        current = self.buffer.head  # set the head to a variable
        while (current is not None):  # while current
            box.append(current.value)  # move the current into the box
            current = current.next  # move the head and start over
        return box  # return the box
