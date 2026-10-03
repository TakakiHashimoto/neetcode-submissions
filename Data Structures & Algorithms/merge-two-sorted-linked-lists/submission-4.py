# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        current = list1 if list1.val <= list2.val else list2
        
        head = current
        next_candidate1 = None
        next_candidate2 = None
        if list1.val <= list2.val:
            next_candidate1 = current.next
            next_candidate2 = list2
        else:
            next_candidate1 = list1
            next_candidate2 = current.next

        while next_candidate1 and next_candidate2:
            if next_candidate1.val < next_candidate2.val:
                current.next = next_candidate1
                current = next_candidate1
                next_candidate1 = next_candidate1.next
            else:
                current.next = next_candidate2
                current = next_candidate2
                next_candidate2 = next_candidate2.next

        current.next = next_candidate1 if next_candidate1 else next_candidate2
        
        return head