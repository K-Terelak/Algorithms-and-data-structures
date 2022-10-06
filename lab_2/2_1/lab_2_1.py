class Queue:
    arr = []
    len = 0

    # add element to queue
    def queue(self, obj):
        self.arr += [obj]
        self.len += 1
        return

    # remove element from queue
    def dequeue(self):
        if self.len == 0:
            raise IndexError("Queue is empty")
        ret = self.arr[0]
        self.arr = self.arr[1:]
        self.len -= 1
        return ret

    # get element from queue
    def index(self, i):
        if i >= self.len or i < 0:
            raise IndexError("Index error")
        return self.arr[i]


q = Queue()
q.queue(2)
q.queue(1)
q.queue(3)
q.queue(7)
print("dequeue:" + str(q.dequeue()))
print("index[0]: " + str(q.index(0)))
