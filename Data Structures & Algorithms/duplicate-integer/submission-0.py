class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_dict = {}
        for n in nums:
            if n in seen_dict:
                return True
            seen_dict[n] = True
        return False


# Time complexity: O(n) - iterating over nums
# Space complexity: O(n) - hash table