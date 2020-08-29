'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

#1. output list를 만들기 위해 defaultdict() 생성
#2. strs의 각 문자를 sorted
#3. 알파벳 하나하나를 공백을 기준으로 join하여 key값 생성
#4. 원하는건 value 값이므로 append(word)

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for s in strs:
            anagram[''.join(sorted(s))].append(s)
            # print(sorted(s))  # 알파벳 하나하나 구분
        return anagram.values()