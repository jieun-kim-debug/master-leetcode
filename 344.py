#sol1. pythonic
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

#sol2. two pointers
#1. left, right(len-1 index start 0) pointer
#2. while left < right:
#3. s[left] <-> s[right] swap
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1