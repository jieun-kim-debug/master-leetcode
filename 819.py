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
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
        words = [word for word in re.sub('[^\w]', ' ', paragraph.lower().split())
                 if word not in banned]
        # 전처리된 단어를 counter
        count = collections.Counter(words)
        # print(count)
        # ({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})

        # 가장 많은 단어 1위를 가져오는데, key와 value라 [0][0]을 해야만 key값이 출력
        return count.most_common(1)[0][0]