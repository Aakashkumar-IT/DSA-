from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev, cur = head, head.next

        while cur:

            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue

            tmp = dummy

            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next


# Taking input from the user
values = list(map(int, input("Enter the elements: ").split()))

# Creating the linked list
head = None
tail = None

for value in values:
    new_node = ListNode(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


# Calling insertion sort
solution = Solution()
head = solution.insertionSortList(head)


# Displaying the sorted linked list
print("Sorted linked list:")

current = head

while current:
    print(current.val, end=" ")
    current = current.next