# Chapter 2 problem 2
import NodeClass


def return_kth_to_last(head : NodeClass.ListNode, k) -> NodeClass.ListNode:
    n = head
    aux = n

    for i in range(0, k):
        print("node value:", str(aux.value))
        if aux is not None:
            aux = aux.next
        else:
            print("not enough elements")
            return None

    while aux is not None:
        n = n.next
        aux = aux.next

    return n

list_head = NodeClass.ListNode(1)
list_head.next = NodeClass.ListNode(2)
list_head.next.next = NodeClass.ListNode(3)
list_head.next.next.next = NodeClass.ListNode(4)

print(return_kth_to_last(list_head, 4).value)