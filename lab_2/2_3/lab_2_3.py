class Stack:
    arr = []
    len = 0

    # add element to the end of stack
    def append(self, item):
        self.arr = self.arr + [item]
        self.len += 1

    # return and remove last element from stack
    def pop(self):
        self.len -= 1
        popped = self.arr[self.len]
        self.arr = self.arr[:-1]
        return popped

    # get element from stack
    def index(self, i):
        try:
            return self.arr[i]
        except IndexError:
            return IndexError("Index error")


stack = Stack()
stack.append("one")
stack.append("two")
stack.append("three")
print("index(2): " + stack.index(2))
while stack.len > 0:
    print(stack.pop())
