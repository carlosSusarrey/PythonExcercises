# Chapter 2 problem 7
import NodeClass


def return_intersection_node(head1: NodeClass.ListNode, head2: NodeClass.ListNode):
    size1 = NodeClass.get_list_size(head1)
    size2 = NodeClass.get_list_size(head2)

    difference = size1 - size2

    if difference > 0:
        curr_long_list = head1
        curr_short_list = head2
    else:
        curr_long_list = head2
        curr_short_list =head1

    for i in range(0, abs(difference)):
        curr_long_list = curr_long_list.next

    while curr_long_list is not None:
        if curr_long_list.__eq__(curr_short_list):
            return curr_long_list
        curr_long_list = curr_long_list.next
        curr_short_list = curr_short_list.next

    return None

list_head = NodeClass.ListNode(7)
list_head.next = NodeClass.ListNode(4)
list_head.next.next = NodeClass.ListNode(3)

list_head1 = NodeClass.ListNode(2)
list_head1.next = NodeClass.ListNode(3)
list_head1.next.next = list_head

list_head2 = NodeClass.ListNode(2)
list_head2.next = list_head

print(return_intersection_node(list_head1, list_head2).value)