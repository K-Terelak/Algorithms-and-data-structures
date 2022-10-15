class Node:
    previous = None
    data = None
    next = None

    def __init__(self, d, previous_node=None, next_node=None):
        self.data = d
        self.previous = previous_node
        self.next = next_node


class List:
    start = None
    len = 0

    # util, return previous element from list
    def get_previous_node(self, i):
        current_node = self.start
        for i in range(1, i):
            current_node = current_node.next
        return current_node

    # add element to List with index
    def insert(self, item, i):
        # 1 insert node to the beginning of a ist
        if i == 0:
            old_start = self.start
            newNode = Node(item, None, old_start)
            if self.len > 0:  # insert node before existing elements
                self.start = newNode
                old_start.previous = newNode
            else:  # add first node (list empty)
                self.start = newNode

        # 2 insert node to the end of list
        elif i == self.len:
            previous_node = self.get_previous_node(self.len)
            previous_node.next = Node(item, previous_node, None)

        # 3 insert node inside list
        elif i < self.len:
            before = self.get_previous_node(i)
            after = before.next
            newNode = Node(item, before, after)
            before.next, after.previous = newNode, newNode
        else:
            return IndexError("Index error")
        self.len += 1

    def removeAt(self, i):
        # 1  remove first node
        if i == 0:
            self.start = self.start.next
            self.start.previous = None

        # 2 remove last node
        elif i == self.len - 1:
            penultimate_node = self.get_previous_node(i)
            penultimate_node.next = None

        # remove node inside list
        elif i < self.len:
            previous_node = self.get_previous_node(i)
            next_node = previous_node.next.next
            previous_node.next, next_node.previous = next_node, previous_node
        else:
            return IndexError("Index error")
        self.len -= 1

    # get element at given index
    def elemAt(self, i):
        try:
            current = self.start
            for i in range(1, i + 1):
                current = current.next
            return current.data
        except Exception:
            return

    # print streamList (for testing)
    def print_list(self):
        print("\nStreamList:")
        current_node = self.start
        for i in range(0, self.len):
            print(str(i) + " " + str(current_node.data))
            current_node = current_node.next


ls = List()
ls.insert('b', 0)  # [b]
ls.insert('a', 0)  # [a, b]
ls.insert('d', 2)  # [a, b, d]
ls.insert('c', 2)  # [a, b, c, d]
ls.insert('e', 4)  # [a, b, c, d, e]
ls.removeAt(0)  # [b, c, d, e]
ls.removeAt(1)  # [b, d, e]
print(ls.elemAt(0))  # b
print(ls.elemAt(1))  # d
print(ls.elemAt(2))  # e
print(ls.elemAt(3))  # not found
ls.print_list()
