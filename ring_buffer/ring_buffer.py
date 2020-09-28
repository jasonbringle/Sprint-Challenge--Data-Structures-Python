class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.current = 0

    def append(self, item):
        if len(self.arr) < self.capacity:
            self.arr.append(item)
        else:
            self.arr[self.current] = item
            self.current = (self.current + 1) % self.capacity


    def get(self):
        return self.arr
        