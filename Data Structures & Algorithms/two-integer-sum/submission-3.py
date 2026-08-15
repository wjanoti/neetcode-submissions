class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                # seen only has indexes smaller than i, so it needs to be the first element in the return.
                return[seen[diff], i]
            seen[val] = i
