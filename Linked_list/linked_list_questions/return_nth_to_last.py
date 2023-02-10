"""
Implement an algorithm to find the nth to last element of a singly linked list.
"""
from linked_list_for_questions import LinkedList


# My initial solution
def return_nth_element_from_last(ll, n):  # TC O(n) SC O(1)
    if ll.head is None:
        return

    pointer_1 = ll.head
    pointer_2 = ll.head

    count = 0

    while count < n:
        if pointer_2 is None:
            return 'The length of LL is not enough to cover the n parameter'
        pointer_2 = pointer_2.next
        count += 1

    while pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    return pointer_1


# Course solution
def return_nth_element_from_last_2(ll, n):
    pointer_1 = ll.head
    pointer_2 = ll.head

    for i in range(n):
        if pointer_2 is None:
            return None
        pointer_2 = pointer_2.next

    while pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    return pointer_1


tests_linked_list = LinkedList()
tests_linked_list.generate(10, 0, 99)
print(tests_linked_list)
print(return_nth_element_from_last_2(tests_linked_list, 2))
