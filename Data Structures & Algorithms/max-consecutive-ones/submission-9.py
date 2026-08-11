class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = -1
        current_consecutive_ones = 0
        for n in nums:
            if n == 1:
                current_consecutive_ones += 1
            else:
                current_consecutive_ones = 0
            max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
        return max_consecutive_ones