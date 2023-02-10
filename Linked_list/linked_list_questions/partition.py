"""
Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or equal to x.
"""
from linked_list_for_questions import LinkedList


def partition(ll, x):  # TC O(n) SC O(1)
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = None

        if curr_node.value < x:
            curr_node.next = ll.head
            ll.head = curr_node
        else:
            ll.tail.next = curr_node
            ll.tail = curr_node
        curr_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None


test_linked_list = LinkedList()
test_linked_list.generate(10, 0, 99)

print(test_linked_list)
partition(test_linked_list, 30)
print(test_linked_list)
