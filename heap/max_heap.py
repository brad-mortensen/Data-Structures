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
        parent = (index-1)//2
        if index < 1:
            return
        elif self.storage[index] > self.storage[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _sift_down(self, index):
        l_child = index*2+1
        r_child = index*2+2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)



my_heap = Heap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(8)

print(f'my heap: {my_heap.storage}')
