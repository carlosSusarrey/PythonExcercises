# Chapter 2 problem 1
import NodeClass


def remove_dups(head: NodeClass.ListNode):
    """

    :type head: ListNode
    """
    if head is None:
        return None

    n = head

    while n is not None:
        aux = n
        while aux.next is not None:
            if aux.next.value == n.value:
                aux.next = aux.next.next
            else:
                aux = aux.next

        n = n.next

list_head = NodeClass.ListNode(1)
list_head.next = NodeClass.ListNode(1)
list_head.next.next = NodeClass.ListNode(1)

remove_dups(list_head)

n = list_head
while n is not None:
    print(n.value)
    n = n.next