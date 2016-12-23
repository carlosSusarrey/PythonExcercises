# Chapter 2 problem 6
import NodeClass
import math


def is_palindrome(head: NodeClass.ListNode):
    list_size = NodeClass.get_list_size(head)
    steps = math.ceil(list_size/2)

    if (list_size % 2) == 0:
        list_has_even_size = True
    else:
        list_has_even_size = False

    work_node = head
    stored_values_stack = []

    for i in range(0, steps):
        stored_values_stack.append(work_node.value)
        work_node = work_node.next

    if not list_has_even_size:
        stored_values_stack.pop()

    while work_node is not None:
        if stored_values_stack.pop() != work_node.value:
            return False
        work_node = work_node.next
    return True


list_head = NodeClass.ListNode(2)
list_head.next = NodeClass.ListNode(3)
list_head.next.next = NodeClass.ListNode(2)

n = is_palindrome(list_head)


print(n)