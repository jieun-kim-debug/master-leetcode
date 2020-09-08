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