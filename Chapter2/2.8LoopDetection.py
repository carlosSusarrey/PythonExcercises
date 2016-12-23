# Chapter 2 problem 8
import NodeClass


def detect_looped_node(head: NodeClass.ListNode):
    slow = head
    fast = head
    looped = False

    while fast.next is not None and not looped:

        fast = fast.next.next
        slow = slow.next
        if slow.__eq__(fast):
            looped = True



    slow = head
    if not looped:
        return None

    while slow is not None:
        if slow.__eq__(fast):
            return fast

        slow = slow.next
        fast = fast.next

begin = NodeClass.ListNode(-1)
additional = NodeClass.ListNode(0)
list_head = NodeClass.ListNode(1)
node1 = NodeClass.ListNode(2)
node2 = NodeClass.ListNode(3)
node3 = NodeClass.ListNode(4)

begin .next = additional
additional.next = list_head
list_head.next = node1
node1.next = node2
node2.next = node3
node3.next = begin

print(detect_looped_node(begin).value)

