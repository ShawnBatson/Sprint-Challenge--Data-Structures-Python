from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = DoublyLinkedList()
        self.current = None
        self.length = 0

    def append(self, item):
        if (self.length == self.capacity):
            if self.current.next is not None:
                self.current.value = item
                self.current = self.current.next
            elif self.current.next is None:
                self.buffer.value = item
                self.current = self.buffer.head
        else:
            self.buffer.add_to_tail(item)
            self.current = self.buffer.head
            self.length += 1

    def get(self):
        list_buffer_contents = []
        current = self.buffer.head
        while (current is not None):
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents
