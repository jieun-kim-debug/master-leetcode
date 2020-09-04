#1. 양방향에서 데이터 처리할 수 있는 deque 이용
#2. node가 존재하는 동안 node의 값이 q.append
#3. node=node.next
#4. q에 양끝쪽이 같지 않으면 false
#5. return True

import collections
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
        
        # 예외처리!
        if not head:
            return True
        
        node = head
        
        while node:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True