class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        if self.get_size() == 1:
            return self.storage.pop()
        top_node = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return top_node

    def get_max(self):
        if self.storage:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = (index-1)//2
        if index < 1:
            return
        elif self.storage[index] > self.storage[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _sift_down(self, index):
        l = index*2+1
        r = index*2+2
        top = index
        if self.get_size() > l and self.storage[top] < self.storage[l]:
            top = l
        if self.get_size() > r and self.storage[top] < self.storage[r]:
            top = r
        if top != index:
            self._swap(index, top)
            self._sift_down(top)


my_heap = Heap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(8)

print(f'my heap: {my_heap.storage}')
