'''
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#sol1. recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # set next node & current node to params
        def reverse(node: ListNode, prev: ListNode = None):
            
            # case node=None
            if not node:
                return prev
            
            curr, node.next = node.next, prev
            return reverse(curr, node)
        
        return reverse(head)
    
#sol2. iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            curr, node.next = node.next, prev
            prev, node = node, curr
            
        return prev