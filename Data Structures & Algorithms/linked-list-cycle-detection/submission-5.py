# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        already_nexted = set()
        while current:
            if current.next in already_nexted:
                return True
            already_nexted.add(current.next)
            current = current.next
        
        return False

# ChatGPT solution
