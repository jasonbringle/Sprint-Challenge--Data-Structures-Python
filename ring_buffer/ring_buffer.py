class RingBuffer:
    def __init__(self, capacity):
        #Maximum capacity of array
        self.capacity = capacity
        #Array
        self.arr = []
        #Current positiion in array
        self.current = 0

    def append(self, item):
        #Check if the length of the array is less than the capacity of the array
        if len(self.arr) < self.capacity:
            #append the item
            self.arr.append(item)
        #Otherwise assign the item to the current position in the array
        else:
            self.arr[self.current] = item
            #Then change the current position to plus on and modulo it against the capacity.  This way it will return the position + 1 except if it is the head (no item present) or the tail (the end of the array.  Which will return it to the begining of the array (0))
            self.current = (self.current + 1) % self.capacity


    def get(self):
        #Return the array
        return self.arr
        