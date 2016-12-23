# Chapter 2 problem 1
import NodeClass


def remove_dups(head: NodeClass.ListNode):
    """

    :type head: ListNode
    """
    if head is None:
        return None

    work_node = head

    while work_node is not None:
        auxiliary_node = work_node
        while auxiliary_node.next is not None:
            if auxiliary_node.next.value == work_node.value:
                auxiliary_node.next = auxiliary_node.next.next
            else:
                auxiliary_node = auxiliary_node.next

        work_node = work_node.next

list_head = NodeClass.ListNode(1)
list_head.next = NodeClass.ListNode(1)
list_head.next.next = NodeClass.ListNode(1)

remove_dups(list_head)

n = list_head
while n is not None:
    print(n.value)
    n = n.next