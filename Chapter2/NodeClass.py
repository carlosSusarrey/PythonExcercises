# This is file contains the Node classes that will be used in this project


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        return id(self) == id(other)


def get_list_size(head: ListNode):
    iterator = head
    count = 0
    while iterator is not None:
        count += 1
        iterator = iterator.next
    return count