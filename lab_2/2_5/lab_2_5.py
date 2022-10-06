class Node:
    previous = None
    data = None
    next = None

    def __init__(self, d, before=None, after=None):
        self.data = d
        self.previous = before
        self.next = after


class List:
    start = None
    len = 0

    # util, return previous element from list
    def get_previous_node(self, i):
        current = self.start
        for i in range(1, i):
            current = current.next
        return current

    # add element to List with index
    def insert(self, item, i):

        # 1 insert node to the beginning of a ist
        if i == 0:
            old_first = self.start
            self.start = Node(item)
            if self.len > 0:
                self.start.next = old_first

        # 2 insert node to the end of list
        if i == self.len:
            before = self.get_previous_node(self.len)
            before.next = Node(before, item, None)

        # 3 insert node inside list
        elif i < self.len:
            before = self.get_previous_node(i)
            after = before.next.next
            after.previous = Node(item)
            before.next = Node(item)
        else:
            return IndexError("Index error")
        self.len += 1

    #     TODO

    # print streamList (for testing)
    def print_list(self):
        try:
            print("\nPrint")
            current_node = self.start
            for i in range(0, self.len):
                print(str(i) + " " + current_node.data)
                current_node = current_node.next_node
        except AttributeError:
            return


ls = List()
ls.insert('a', 0)
ls.insert('b', 1)
ls.insert('c', 2)
ls.insert('d', 3)
ls.print_list()
