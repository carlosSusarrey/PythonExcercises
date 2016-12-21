# Chapter 2 problem 3
import NodeClass


def delete_middle_node(node: NodeClass.ListNode):
    if node.next is None or node is None:
        print("Can't remove last node")
        return False

    node.value = node.next.value
    node.next = node.next.next
    return True

list_head = NodeClass.ListNode(1)
list_head.next = NodeClass.ListNode(2)
list_head.next.next = NodeClass.ListNode(3)
list_head.next.next.next = NodeClass.ListNode(4)

delete_middle_node(list_head)

n = list_head
while n is not None:
    print(n.value)
    n = n.next