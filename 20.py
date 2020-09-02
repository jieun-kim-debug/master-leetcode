#1. 매핑 table 값과 input 값 매칭
#2. 매핑 table에 값이 없으면 stack에 push
#3. tabel value 값과 일치 하지 않으면 False
#4. input과 table value 값이 일치하면 pop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
            
        return len(stack)==0