# Chapter 2 problem 5
import NodeClass


def sum_list_forward(head1: NodeClass.ListNode, head2: NodeClass.ListNode):
    carry = 0
    difference = NodeClass.get_list_size(head1) - NodeClass.get_list_size(head2)

    if difference < 0:
        head1 = insert_zero_nodes(head1, abs(difference))
    elif difference > 0:
        head2 = insert_zero_nodes(head2, difference)

    sum_head = sum_list_forward_recursive(head1, head2)
    if sum_head.value > 9:
        sum_head = insert_before(sum_head, 1)

    return sum_head


def sum_list_forward_recursive(node1: NodeClass.ListNode, node2: NodeClass.ListNode)-> NodeClass.ListNode:
    if node1.next is None:
        new_node = NodeClass.ListNode(node1.value + node2.value)
        return new_node

    sum = NodeClass.ListNode(0)
    sum.next = sum_list_forward_recursive(node1.next, node2.next)
    if sum.next.value > 9:
        sum.value = node1.value + node2.value + 1
        sum.next.value %= 10
    else:
        sum.value = node1.value + node2.value
    return sum


def insert_zero_nodes(head: NodeClass.ListNode, count):
    new_head = head
    for i in range(0, count):
        new_head = insert_before(head, 0)
    return new_head


def insert_before(head: NodeClass.ListNode, val):
    temp = NodeClass.ListNode(val)
    temp.next = head
    return temp





def sum_list_back(head1: NodeClass.ListNode, head2: NodeClass.ListNode):
    carry = 0
    sum_node = None
    sum_head = None
    while head1 is not None or head2 is not None:
        if head1 is None:
            head1 = NodeClass.ListNode(0)
        if head2 is None:
            head2 = NodeClass.ListNode(0)

        sum = head1.value + head2.value + carry
        if sum > 9:
            carry = 1
        else:
            carry = 0

        if sum_node is None:
            sum_node = NodeClass.ListNode(sum % 10)
            sum_head = sum_node
        else:
            sum_node.next = NodeClass.ListNode(sum % 10)
            sum_node = sum_node.next

        head1 = head1.next
        head2 = head2.next
    return sum_head

list_head = NodeClass.ListNode(3)
list_head.next = NodeClass.ListNode(9)
list_head.next.next = NodeClass.ListNode(1)

list_head2 = NodeClass.ListNode(3)
list_head2.next = NodeClass.ListNode(2)

n = sum_list_forward(list_head, list_head2)

while n is not None:
    print(n.value)
    n = n.next

# 6->1->1
# 5->2->3
#116 = 325 = 441
#
# 611 + 523 = 1134

print()
