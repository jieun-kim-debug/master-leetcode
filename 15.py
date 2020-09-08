#sol1. two pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        # two pointers shift sorted list 
        nums.sort()
        
        # 3 variables iteration
        for i in range(len(nums)-2):
            # skip variable i duplicated value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # set initial location to two pointers
            left, right = i+1, len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # two pointers shifting condition
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append((nums[i], nums[left], nums[right]))
                    
                    # avoid left pointer duplicated value
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # avoid right pointer duplicated value
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                        
                    # condition of first while sentence
                    left += 1
                    right -= 1
                    
        return results