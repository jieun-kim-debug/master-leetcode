'''
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

#1. 슬라이딩 윈도우로 투 포인터 함수 생성
#2. s[left]==s[right] 일때의 포인터를 return
#3. 문자열 인덱스 유의해서 return
#4. 팰린드롬이 안될 경우 if문
#5. 결과값을 res라는 빈 문자열에 저장

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        if len(s)<2 or s==s[::-1]:
            return s            
        
        res = ''
        for p in range(len(s)-1):
            res = max(res, expand(p,p), expand(p,p+1), key=len)
        
        return s