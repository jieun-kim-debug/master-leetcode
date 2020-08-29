class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1. split로 나누기
        #2. 리스트 내 중복요소 찾기
        #3. 가장 많이 나온 중복요소 print
        a = []
        a.append(paragraph.split())
        # print(a)
        