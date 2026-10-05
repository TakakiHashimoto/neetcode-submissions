# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pairs = {}
        current = head
        index = 1
        head = head
        while current:
            pairs[index] = current
            current = current.next
            index += 1

        end = len(pairs)
        previous_index = end - n
        next_index = previous_index + 2
        if previous_index <=0:
            if next_index > end:
                return None
            return pairs[next_index]

        if next_index > end:
            pairs[previous_index].next = None
            return head

        pairs[previous_index].next = pairs[next_index]


        return head 
        