# Chapter 2 problem 4
import NodeClass


def partition_list(head: NodeClass.ListNode, value):
    left_begin = head
    right_end = head
    current = head

    while current is not None:
        temp = current.next
        if current.value < value:
            current.next = left_begin
            left_begin = current
        else:
            right_end.next = current
            right_end = right_end.next
        current = temp

    right_end.next = None

    return left_begin


def partition_list_in_order(head: NodeClass.ListNode, value):
    left_begin = None
    left_end = None
    right_begin = None
    right_end = None

    while head is not None:
        temporarily_saved_node = head.next
        head.next = None
        if head.value < value:
            if left_begin is None:
                left_begin = head
                left_end = left_begin
            else:
                left_end.next = head
                left_end = left_end.next
        else:
            if right_begin is None:
                right_begin = head
                right_end = right_begin
            else:
                right_end.next = head
                right_end = right_end.next
        head = temporarily_saved_node

    if left_begin is None:
        return right_begin

    left_end.next = right_begin
    return left_begin


list_head = NodeClass.ListNode(3)
list_head.next = NodeClass.ListNode(2)
list_head.next.next = NodeClass.ListNode(1)
list_head.next.next.next = NodeClass.ListNode(4)

n = partition_list(list_head, 3)

while n is not None:
    print(n.value)
    n = n.next

# 3>4>5
# head = 3
# tail = 3
#
#
#
