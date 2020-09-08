'''Input:  [1,2,3,4]
Output: [24,12,8,6]'''

#sol1. except self multiple array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set empty array
        output = []
        
        # initial multiply 1
        p = 1
        # from left multiple(except last right element)
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        
        # initial multiply 1
        p = 1    
        # (last index, first index, -1 drop)
        for i in range(len(nums)-1, 0 - 1, -1):
            # update element left * right
            output[i] = output[i] * p
            # from right multiple(except first left element)
            p = p * nums[i]
        
        return output