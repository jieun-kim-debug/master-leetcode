'''
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
'''
#1. paragraph 안 특수문자 제거, 소문자 처리
#2. counter()로 단어 세기
#3. 가장 많이 나온 단어의 인덱스 출력

import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        