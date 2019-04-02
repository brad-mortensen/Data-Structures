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
        node = ListNode(value)
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            self.head = node
            self.tail = node
            self.length += 1

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            old_head = self.head
            new_head = self.head.next
            self.head.delete()
            self.head = new_head
            self.length -= 1
            return old_head

    def add_to_tail(self, value):
        node = ListNode(value)
        if self.head and self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.head = node
            self.tail = node
            self.length += 1

    def remove_from_tail(self):
        if not self.head:
            return None
        else:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
            return old_tail

    def move_to_front(self, node):
        current = self.head
        if not self.head:
            return
        while current:
            if current.value == node:
                new_head = node
                self.head.insert_before(new_head)
                self.head = self.head.prev
                current.delete()
            current = current.next
        return None

    def move_to_end(self, node):
        current = self.tail
        if not self.head or self.tail.value == node:
            return
        while current:
            if current.value == node:
                new_tail = node
                self.tail.insert_after(new_tail)
                self.tail = self.tail.next
                current.delete()
            current = current.prev
        return None

    def delete(self, node):
        if not self.head or not self.tail:
            return None
        current = self.head
        while current:
            if current.value == node:
                current.delete()
                self.length -= 1
            current = current.next

    def get_max(self):
        maximum = -9999999
        current = self.head
        while current:
            if current.value > maximum:
                maximum = current.value
            current = current.next
        return maximum

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ", flush=True)
            current = current.next


dll = DoublyLinkedList()
dll.add_to_tail(1)
dll.print_list()
print('\n')
dll.remove_from_head()
dll.add_to_head(6)
dll.print_list()
print('\n')
