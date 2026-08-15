class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                # prevMap only contains indexes smaller than i, so we need to use it first to satisfy the problem constraint.
                return [prevMap[diff], i]
            prevMap[nums[i]] = i
        

    
