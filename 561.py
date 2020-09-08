#sol1. ascending
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # set variables
        sum = 0
        pair = []
        # ascending list
        nums.sort()
        
        # take out list values
        for n in nums:
            pair.append(n)
            
            # set pair(a,b)
            if len(pair) == 2:
                # min of pair add
                sum += min(pair)
                # initialize pair list                
                pair = []
                
        return sum

#sol2. even number index
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # set variable
        sum = 0
        # ascending nums list
        nums.sort()
        
        # index, value enumerate 
        for i, n in enumerate(nums):
            # even number index(cuz ascending list)
            if i % 2 == 0:
                sum += n
                
        return sum
        