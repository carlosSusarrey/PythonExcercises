# Chapter 2 problem 6
import NodeClass
import math


def is_palindrome(head: NodeClass.ListNode):
    size = NodeClass.get_list_size(head)
    steps = math.ceil(size/2)

    if (size % 2) == 0:
        even = True
    else:
        even = False

    helper = head
    stack = []

    for i in range(0, steps):
        stack.append(helper.value)
        helper = helper.next

    if not even:
        stack.pop()

    while helper is not None:
        if stack.pop() != helper.value:
            return False
        helper = helper.next
    return True


list_head = NodeClass.ListNode(2)
list_head.next = NodeClass.ListNode(3)
list_head.next.next = NodeClass.ListNode(2)

n = is_palindrome(list_head)


print(n)