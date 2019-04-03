class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        pass

    def get_max(self):
        if self.storage:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.storage[index] > self.storage[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _sift_down(self, index):
        pass

my_heap = Heap()
my_heap.insert(4)
