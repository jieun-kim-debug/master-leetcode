# print("b" > "a") True 문자 대소 비교 가능
# set()={} 집합 딕셔너리 자료형 / 중복 불허, 순서x
# join() 리스트에서 문자열으로

#1. input이 순차적으로 들어오다가 char이 stack에 있던 char보다 작을 경우, pop
#2. 중복되는 char이 들어오면 continue하고 pop된 char remove
#3. stack에 쌓인 문자들 join() 

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char<stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
            
            # print(stack)
            # print(seen)
            
        return ''.join(stack)