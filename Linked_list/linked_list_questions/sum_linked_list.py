"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digits is at the head of the list.
Write a function that adds the two numbers and returns the sum as linked list.
"""
from linked_list_for_questions import LinkedList


def sum_ll(list_1, list_2):  # TC O(n) SC O(n)
    n_1 = list_1.head
    n_2 = list_2.head
    carry = 0

    ll = LinkedList()

    while n_1 or n_2:
        result = carry

        if n_1:
            result += n_1.value
            n_1 = n_1.next

        if n_2:
            result += n_2.value
            n_2 = n_2.next

        ll.add(int(result % 10))
        carry = result / 10

    return ll


ll_a = LinkedList()
ll_a.add(7)
ll_a.add(1)
ll_a.add(6)

ll_b = LinkedList()
ll_b.add(5)
ll_b.add(9)
ll_b.add(2)

print(ll_a)
print(ll_b)

print(sum_ll(ll_a, ll_b))

