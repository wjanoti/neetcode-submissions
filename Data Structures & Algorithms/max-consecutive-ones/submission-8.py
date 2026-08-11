class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = -1
        current_consecutive_ones = 0
        for n in nums:
            if n == 1:
                current_consecutive_ones += 1
            elif current_consecutive_ones >= max_consecutive_ones:
                max_consecutive_ones = current_consecutive_ones
                current_consecutive_ones = 0
            else:
                current_consecutive_ones = 0
        return max(max_consecutive_ones, current_consecutive_ones)