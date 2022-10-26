class Node:
    data = None
    next_node = None

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n


class CircularLinkedList:
    first_node = None
    len = 0

    # return previous node at index (util)
    def get_previous_node(self, i):
        currentNode = self.first_node
        for i in range(1, i):
            currentNode = currentNode.next_node
        return currentNode

    # add element to list with index
    def insert(self, data, index):

        # 1  insert node to the beginning of a list
        if index == 0:
            old_first = self.first_node
            self.first_node = Node(data)
            if self.len > 0:  # connect recently added with old first
                self.first_node.next_node = old_first
                # connect last with recently added node
                self.get_previous_node(self.len + 1).next_node = self.first_node

        # 2 insert node to the end of list
        elif index == self.len:
            self.get_previous_node(self.len).next_node = Node(data, self.first_node)

        # 3 insert node inside list
        elif index < self.len:
            previous_node = self.get_previous_node(index)
            previous_node.next_node = Node(data, previous_node.next_node)
        else:
            raise IndexError("Index error :(")
        self.len += 1

    # get element from list at given index
    def elemAt(self, index):
        try:
            if index < 0:
                raise Exception("negative index")
            return self.get_previous_node(index + 1).data
        except Exception:
            return "Index error"

    # remove element from list at given index
    def removeAt(self, index):
        # 1  remove first node
        if index == 0:
            self.first_node = self.first_node.next_node
            self.get_previous_node(self.len - 1).next_node = self.first_node

        # 2 remove last node
        elif index == self.len - 1:
            self.get_previous_node(index).next_node = self.first_node

        # 3 remove node inside list
        elif index < self.len:
            previous_node = self.get_previous_node(index)
            previous_node.next_node = previous_node.next_node.next_node
        else:
            print("Index error")
        self.len -= 1


cl = CircularLinkedList()
cl.insert('b', 0)  # [b]
cl.insert('a', 0)  # [a, b]
cl.insert('c', 2)  # [a, b, c]
cl.insert('e', 3)  # [a, b, c, e]
cl.insert('d', 3)  # [a, b, c, d, e]
cl.insert('3', 1)  # [a, 3 , b, c, d, e]
cl.insert('0', 0)  # [0, a, 3 , b, c, d, e]
cl.insert('7', 7)  # [0, a, 3 , b, c, d, e, 6]
print(cl.elemAt(0))  # 0
print(cl.elemAt(1))  # a
print(cl.elemAt(2))  # 3
print(cl.elemAt(5))  # d
print(cl.elemAt(8))  # 0
print(cl.elemAt(9))  # a
print(cl.elemAt(-1))  # Index error
cl.removeAt(0)  # [a, 3 , b, c, d, e, 7]
cl.removeAt(1)  # [a, b, c, d, e, 7]
cl.removeAt(5)  # [a, b, c, d, e]
