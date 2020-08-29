'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
'''

"""브루투 포스 방식으로 시간 복잡도 O(n**2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
"""

#1. 빈 딕셔너리 생성
#2. enumerate를 써서 키와 값을 바꾸어 딕셔너리로 저장
#3. if target-num in 딕셔너리
#4. 딕셔너리[target-num],index

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps = {}

        for i, num in enumerate(num_maps):
            num_maps[num]=i
            print(num_maps)
        
            if target-num in num_maps:
                return [num_maps[target-num],i]