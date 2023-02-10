"""
Remove duplicates from unsorted linked list.
"""
from linked_list_for_questions import LinkedList


# My initial solution
# def remove_duplicates(ll):
#     if ll.head is None:
#         return
#
#     current_node = ll.head
#     visited_nodes = set()
#
#     while current_node:
#         if current_node.value not in visited_nodes:
#             visited_nodes.add(current_node.value)
#         else:
#             temp_node = ll.head
#             while temp_node:
#                 if temp_node.next == current_node:
#                     break
#                 temp_node = temp_node.next
#             temp_node.next = temp_node.next.next
#         current_node = current_node.next
#     return ll

# More optimised solution
def remove_duplicates(ll):  # TC O(n) SC O(n)
    if ll.head is None:
        return

    current_node = ll.head
    visited_nodes = {current_node.value}

    while current_node.next:
        if current_node.next.value in visited_nodes:
            current_node.next = current_node.next.next
        else:
            visited_nodes.add(current_node.next.value)
            current_node = current_node.next
    return ll


# Without using temporary buffer
def remove_duplicates_2(ll):  # TC O(n^2) SC O(1)
    if ll.head is None:
        return

    current_node = ll.head

    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
    return ll


tests_linked_list = LinkedList()
tests_linked_list.add(1)
tests_linked_list.add(2)
tests_linked_list.add(1)
tests_linked_list.add(3)
tests_linked_list.add(1)
# tests_linked_list.generate(10, 0, 99)
print(tests_linked_list)
# remove_duplicates(tests_linked_list)
remove_duplicates_2(tests_linked_list)
print(tests_linked_list)

# remove_duplicates(tests_linked_list)
