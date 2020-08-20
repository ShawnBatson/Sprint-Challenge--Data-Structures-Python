class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current = self.head  # set the current node
        iterative_previous = None  # set the iterative previous to None
        while current is not None:  # start the while loop
            next_current = current.next_node  # this is the next in line
            # currents next node is set to iterative previous
            current.next_node = iterative_previous
            iterative_previous = current  # set the iterative previous to current
            current = next_current  # set current to the next node
            # set the head to the iterative previous to go backwards.
            self.head = iterative_previous
