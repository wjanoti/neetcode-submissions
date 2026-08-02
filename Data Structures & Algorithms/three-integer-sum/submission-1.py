class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet_map = {}
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                triplet = (nums[i], nums[left], nums[right])
                if s == 0:
                    triplet_map[triplet] = triplet_map.get(triplet, 0) + 1
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
        triplet_list = []
        for k in triplet_map.keys():
            triplet_list.append(list(k))
        return triplet_list

            