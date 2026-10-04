# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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