#1. 각 연결 리스트의 루트를 heap에 저장
#2. 이진 heap 내에서 정렬
#3. heap이 존재하는 동안, 정렬된 구조 pop
#4. 최소힙으로 정렬된 구조를 다시 heappush
#5. return root.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # print(len(lists))
        
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
            # (tuple(list[i]).val==i번째 리스트의 i번째 요소(우선순위), i, i번째 리스트)
                heapq.heappush(heap, (lists[i].val, i , lists[i]))
                # print(f"heap:\n{heap}")
        
        while heap:
            node = heapq.heappop(heap)
            # print(f"node:\n{node}")
            
            idx = node[1]
            # print(f"idx:{idx}")
            result.next = node[2]
            
            result = result.next
            
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
                # print(f"heap:\n{heap}")

                
        return root.next
