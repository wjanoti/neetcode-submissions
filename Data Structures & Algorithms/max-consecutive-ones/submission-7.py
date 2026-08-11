class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = -1
        current_consecutive_ones = 0
        for n in nums:
            print("Current element:", n)
            if n == 1:
                current_consecutive_ones += 1
            elif current_consecutive_ones >= max_consecutive_ones:
                max_consecutive_ones = current_consecutive_ones
                current_consecutive_ones = 0
            else:
                current_consecutive_ones = 0
            print("Current consecutive ones:", current_consecutive_ones)
            print("Max consecutive ones:", max_consecutive_ones)
        return max(max_consecutive_ones, current_consecutive_ones)