class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        i = 0
        triplet_dict = {}
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = len(nums) - 1
            k = i + 1
            while k < j:
                current_sum = nums[i] + nums[k] + nums[j]
                if current_sum == 0:
                    t = (nums[i], nums[k], nums[j])
                    triplet_dict[t] = triplet_dict.get(t, 0) + 1
                    k += 1
                    j -= 1
                elif current_sum > 0:
                    j -= 1
                else:
                    k += 1
        l = []
        for k in triplet_dict.keys():
            l.append(list(k))
        return l