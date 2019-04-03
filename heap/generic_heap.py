class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_priority(self):
        if self.storage:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
