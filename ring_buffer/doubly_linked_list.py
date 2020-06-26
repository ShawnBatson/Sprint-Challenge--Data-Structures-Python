class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        if self.head.next is None:
            self.length -= 1
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        self.length -= 1
        head_value = self.head.value
        self.head = self.head.next
        return head_value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.tail.prev is None:
            self.length -= 1
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        self.length -= 1
        tail_value = self.tail.value
        self.tail = self.tail.next
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        elif node is self.tail:
            old_tail = self.remove_from_tail()
            self.add_to_head(old_tail)
        else:
            old_node = self.delete(node)
            self.add_to_head(old_node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        if node is self.head:
            old_head = self.remove_from_head()
            self.add_to_tail(old_head)
        else:
            old_node = self.delete(node)
            self.add_to_tail(old_node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        data = node.value
        if node == self.head:
            if node.next != None:
                current_head = node
                self.head = current_head.next
                self.head.prev = None
                self.length -= 1
            else:
                self.head = None
                self.tail = None
                self.length = 0
        elif node == self.tail:
            if node.prev != None:
                current_tail = node
                self.tail = current_tail.next
                self.tail.next = None
                self.length -= 1
            else:
                self.head = None
                self.tail = None
                self.length = 0
        else:
            node.delete()
            self.length -= 1
        return data

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head:
            current = self.head
            high_value = self.head.value
            while current.next is not None:
                if current.next.value > high_value:
                    high_value = current.next.value
                current = current.next
            return high_value
