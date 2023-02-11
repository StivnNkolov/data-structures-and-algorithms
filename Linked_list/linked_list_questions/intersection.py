"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node
(by reference) as the jth node of the second linked list, they are intersecting.
"""

from linked_list_for_questions import LinkedList, Node


# My initial solution
def find_intersection(list_a, list_b):
    def find_bigger_list(a, b):
        if len(a) >= len(b):
            return a
        return b

    def find_smaller_list(a, b):
        if len(a) < len(b):
            return a
        return b

    first_list_length = len(list_a)
    second_list_length = len(list_b)

    bigger_list = find_bigger_list(list_a, list_b)
    smaller_list = find_smaller_list(list_a, list_b)

    difference = abs(first_list_length - second_list_length)
    # difference = len(bigger_list) - len(smaller_list)

    bigger_list_starting_node = bigger_list.head
    for index in range(difference):
        bigger_list_starting_node = bigger_list_starting_node.next

    smaller_list_starting_node = smaller_list.head

    while bigger_list_starting_node or smaller_list_starting_node:
        if bigger_list_starting_node == smaller_list_starting_node:
            return bigger_list_starting_node

        bigger_list_starting_node = bigger_list_starting_node.next
        smaller_list_starting_node = smaller_list_starting_node.next

    return False


def second_personal_solution(list_a, list_b):
    def return_intersection_node(first_start_node, second_start_node):
        while first_start_node is not second_start_node:
            first_start_node = first_start_node.next
            second_start_node = second_start_node.next
        return first_start_node

    def find_bigger_list_starting_node(arr, diff):
        curr_node = arr.head
        for index in range(diff):
            curr_node = curr_node.next

        return curr_node

    first_list_len = len(list_a)
    second_list_len = len(list_b)

    if first_list_len == second_list_len:
        return return_intersection_node(list_a.head, list_b.head)
    else:
        bigger_list = list_b if first_list_len < second_list_len else list_a
        smaller_list = list_a if first_list_len < second_list_len else list_b
        difference = len(bigger_list) - len(smaller_list)

        bigger_list_start_node = find_bigger_list_starting_node(bigger_list, difference)
        smaller_list_start_node = smaller_list.head

        return return_intersection_node(bigger_list_start_node, smaller_list_start_node)


# Course solution
"""
Here the time complexity is O(a + b) because we need to find the length of both LL.
To find the length we need to traverse both of them.
"""


def intersection(ll_a, ll_b):  # TC O(a+b) SC O(1)
    if ll_a.tail is not ll_b.tail:
        return False

    len_a = len(ll_a)
    len_b = len(ll_b)

    shorter = ll_a if len_a < len_b else ll_b
    longer = ll_b if len_a < len_b else ll_a

    diff = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


# Helper function to create two linked lists with some same nodes.
def add_same_node(lla, llb, value):
    temp_node = Node(value)
    lla.tail.next = temp_node
    lla.tail = temp_node
    llb.tail.next = temp_node
    llb.tail = temp_node


llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(3, 0, 10)

add_same_node(llA, llB, 11)
add_same_node(llA, llB, 14)

print(llA)
print(llB)

print(find_intersection(llA, llB))
