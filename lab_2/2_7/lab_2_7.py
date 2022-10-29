class Node:
    data = None
    next_node = None

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n


class SentinelLinkedList:
    first_node = None
    len = 0

    # add sentinel node
    def __init__(self):
        self.first_node = Node(None, None)

    # return previous node at index (util)
    def get_previous_node(self, index):
        current_node = self.first_node
        for index in range(1, index):
            current_node = current_node.next_node
        return current_node

    # add element to list with index
    def insert(self, data, index):

        # 1  insert node to the beginning of a list
        if index == 0:
            self.first_node = Node(data, self.first_node)

        # 2 insert node inside or at the end of list
        elif self.len >= index > 0:
            previous_node = self.get_previous_node(index)
            previous_node.next_node = Node(data, previous_node.next_node)
        else:
            raise IndexError("Index error :(")
        self.len += 1

    # remove element from list at given index
    def removeAt(self, index):

        # 1  remove first node
        if index == 0:
            self.first_node = self.first_node.next_node

        # 2 remove node inside or at the end of list
        elif 0 < index <= self.len:
            prev = self.get_previous_node(index)
            prev.next_node = prev.next_node.next_node
        self.len -= 1

    def index(self, index):
        try:
            if index < 0 or index >= self.len:
                raise IndexError("Index Error")
            return self.get_previous_node(index + 1).data
        except Exception as e:
            return e


sl = SentinelLinkedList()
sl.insert('c', 0)  # [c, *sentinel*]
sl.insert('a', 0)  # [a, c, *sentinel*]
sl.insert('b', 1)  # [a, b, c, *sentinel*]
sl.insert('d', 3)  # [a, b, c, d, *sentinel*]
sl.insert('e', 4)  # [a, b, c, d, e, *sentinel*]
sl.insert('f', 5)  # [a, b, c, d, e, f, *sentinel*]
sl.removeAt(0)  # [b, c, d, e, f *sentinel*]
sl.removeAt(1)  # [b, d, e, f *sentinel*]
sl.removeAt(1)  # [b, e, f, *sentinel*]
print(sl.index(-1))  # IndexError
print(sl.index(0))  # b
print(sl.index(1))  # e
print(sl.index(2))  # f
print(sl.index(3))  # IndexError
