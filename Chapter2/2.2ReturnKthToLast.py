# Chapter 2 problem 2
import NodeClass


def return_kth_to_last(head : NodeClass.ListNode, k) -> NodeClass.ListNode:
    work_node = head
    auxiliary_fast_node = work_node

    for i in range(0, k):
        print("node value:", str(auxiliary_fast_node.value))
        if auxiliary_fast_node is not None:
            auxiliary_fast_node = auxiliary_fast_node.next
        else:
            print("not enough elements")
            return None

    while auxiliary_fast_node is not None:
        work_node = work_node.next
        auxiliary_fast_node = auxiliary_fast_node.next

    return work_node

list_head = NodeClass.ListNode(1)
list_head.next = NodeClass.ListNode(2)
list_head.next.next = NodeClass.ListNode(3)
list_head.next.next.next = NodeClass.ListNode(4)

print(return_kth_to_last(list_head, 4).value)