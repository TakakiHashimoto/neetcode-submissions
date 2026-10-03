# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# node0 = {val: 0, next: node1}
# node1 = {val: 1, next: node2}
# node2 = {val: 2, next: node3}
# node3 = {val: 3, node: None}

# My solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            placeholder = current.next
            current.next = previous
            previous = current
            current = placeholder

        return previous