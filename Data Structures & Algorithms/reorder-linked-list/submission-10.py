# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My sol
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pairs = {}
        current = head
        index = 1

        while current:
            pairs[index] = current
            index += 1
            current = current.next

        index = 1
        back_index = len(pairs)
        front = pairs[index]
        back = pairs[back_index]
        
        while index < back_index:
            front.next = back
            index += 1
            front = pairs[index]
            back.next = front
            back_index -= 1
            back = pairs[back_index]

        pairs[(len(pairs) // 2) + 1].next = None

# ChatGPT sol:
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse the second half
        second = slow.next
        slow.next = None

        previous = None
        current = second

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        second = previous
        first = head

        # 3. Merge the two halves alternately
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next