'''
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#sol1. Recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # point = sorted list
        if (not l1) or (l2 and l1.val > l2.val):
            # swap
            l1, l2 = l2, l1
        
        # 11=none stop recursive
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
            
        return l1