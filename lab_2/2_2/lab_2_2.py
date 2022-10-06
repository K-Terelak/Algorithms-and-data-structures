class PriorityQueue:
    arr = []
    len = 0

    # add element to queue with priority
    def queue(self, obj, priority):
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
            self.len -= 1
            return self.arr.pop(0)
        except IndexError:
            return IndexError("IndexError dequeue")

    # get element from a queue
    def index(self, i):
        try:
            return self.arr[i]
        except IndexError:
            return IndexError("IndexError index(%i)" % i)


test = PriorityQueue()
test.queue(3, 3)
test.queue(4, 1)
test.queue(5, 2)
test.queue(1, 4)
test.queue(7, 3)
print(test.arr)
while test.len > 0:
    print(test.dequeue())
