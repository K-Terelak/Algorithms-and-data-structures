class PriorityQueue:
    arr = []
    len = 0

    # add element to queue with priority
    def enqueue(self, obj, priority):
        i = 0
        try:
            while True:
                if self.arr[i][1] < priority:
                    self.arr = self.arr[:i] + [[obj, priority]] + self.arr[i:]
                    self.len += 1
                    break
                i += 1
        except IndexError:
            self.arr = self.arr + [[obj, priority]]
            self.len += 1

    # remove element from queue
    def dequeue(self):
        try:
            popped = self.arr[0]
            self.arr = self.arr[1:]
            self.len -= 1
            return popped
        except IndexError:
            return IndexError("IndexError dequeue")

    # get element from a queue
    def index(self, i):
        try:
            return self.arr[i]
        except IndexError:
            return IndexError("IndexError index(%i)" % i)


test = PriorityQueue()
test.enqueue(3, 3)
test.enqueue(4, 1)
test.enqueue(5, 2)
test.enqueue(1, 4)
test.enqueue(7, 3)
while test.len > 0:
    print(test.dequeue())
