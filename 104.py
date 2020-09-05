#1. root가 없다면 return 0 (예외처리)
#2. 양방향 추출 가능한 deque 자료형, depth=0(초기화)
#3. deque에는 이진트리 형식으로 저장되므로 queue가 있을 때, depth += 1
#4. len(queue)만큼 for문 돌리기
#5. 가장 위쪽에 있는 queue.popleft = 현재 root
#6. aueue 연산 추출 노드의 자식 노드 삽입
#7. return depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
       
        if root is None:
            return 0
    
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # print(f"queue:\n{queue}")
            # deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, 
            # right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, 
            # right: TreeNode{val: 7, left: None, right: None}}}])
 
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
                
        return depth
            