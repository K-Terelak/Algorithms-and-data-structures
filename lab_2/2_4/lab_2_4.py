class Node:
    data = None
    next_node = None

    def __init__(self, d):
        self.data = d


class StreamList:
    first_node = None
    len = 0

    # return node at index
    def get_previous_node(self, i):
        current_node = self.first_node
        for index in range(1, i):
            current_node = current_node.next_node
        return current_node

    # add element to streamList with index
    def insert(self, item, i):

        # 1  insert node to the beginning of a list
        if i == 0:
            old_first = self.first_node
            self.first_node = Node(item)
            if self.len > 0:
                self.first_node.next_node = old_first

        # 2 insert node to the end of list
        elif i == self.len:
            self.get_previous_node(self.len).next_node = Node(item)

        # 3 insert node inside list
        elif i < self.len:
            current_node = self.get_previous_node(i)
            current_node.next_node, current_node.next_node.next_node = Node(item), current_node.next_node
        else:
            print("Index error")
        self.len += 1

    # remove element from streamList with index
    def removeAt(self, i):
        # 1  remove first node
        if i == 0:
            self.first_node = self.first_node.next_node

        # 2 remove last node
        elif i == self.len - 1:
            self.get_previous_node(i).next_node = None
        # remove node inside list
        elif i < self.len:
            current_node = self.get_previous_node(i)
            current_node.next_node = current_node.next_node.next_node
        else:
            return IndexError("Index error")
        self.len -= 1

    # get element from streamList
    def elemAt(self, i):
        try:
            return self.get_previous_node(i + 1).data
        except IndexError:
            return IndexError("Index out of range")

    # print streamList (for testing)
    def print_list(self):
        try:
            print("\nStreamList:")
            current_node = self.first_node
            for i in range(0, self.len):
                print(str(i) + " " + current_node.data)
                current_node = current_node.next_node
        except AttributeError:
            return


streamList = StreamList()
streamList.insert('b', 0)
streamList.insert('a', 0)
streamList.insert('c', 2)
streamList.insert('f', 3)
streamList.insert('e', 3)
streamList.insert('d', 3)
streamList.print_list()  # [a,b,c,d,e,f]

streamList.removeAt(0)
streamList.removeAt(1)
streamList.removeAt(2)
streamList.print_list()  # [b,d,f]

print("\n elemAt")
print(streamList.elemAt(0))  # b
print(streamList.elemAt(1))  # d
print(streamList.elemAt(2))  # f
