#sol1. list

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome=앞뒤가 똑같은 문자열
        #1. strs를 빈리스트에 담기
        #2. 주어진 str에 영문자, 숫자 여부가 있다면, 빈 리스트에 담기
        #3. 모두 소문자로 바꿔줘서 붙이기
        #4. strs의 요소가 1보다 클 때까지 리스트 맨 앞, 맨 뒤 요소 같은지 체크
        #5. 같지 않으면 return False

        strs = []
        for c in s:
             if c.isalnum():
               strs.append(c.lower())
        # print(strs)
        
        # pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제 
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False
        return True

#sol2. deque

import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs : Deque = collections.deque()

        for char in str:
            if char.isalnum():
                strs.append(char.lower())

            while len(strs) > 1:
                strs.popleft() != strs.pop()
                return False
        
        return True