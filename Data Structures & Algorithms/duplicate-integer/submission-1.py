class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Time complexity: O(n) - iterating over nums
# Space complexity: O(n) - hash table