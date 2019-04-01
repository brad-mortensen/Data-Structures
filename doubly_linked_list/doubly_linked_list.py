"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


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

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current = self.head
            current.prev = new_node
            new_node.prev = None
            new_node.next = current
            self.head = new_node
            self.length += 1

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            current = self.head
            self.head = current.next
            self.length -= 1

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            new_node.next = None
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        if not self.head:
            return None
        else:
            current = self.tail
            self.tail = current.prev
            current = self.tail
            current.next = None
            self.length -= 1

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ", flush=True)
            current = current.next

dll = DoublyLinkedList()
dll.add_to_head('candy')
dll.add_to_tail(1)
dll.add_to_tail(2)
dll.add_to_tail(3)
dll.add_to_head('sketi')
dll.add_to_tail(4)
print('\n')
dll.print_list()
print('\n')
dll.remove_from_head()
dll.print_list()
print('\n')
dll.remove_from_tail()
dll.remove_from_tail()
dll.remove_from_head()
dll.print_list()
print('\n')
print(f'List Length: {dll.length}')
print('\n')
