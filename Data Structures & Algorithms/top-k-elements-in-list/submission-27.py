class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}
        for n in nums:
            top[n] = top.setdefault(n, 0) + 1
        sorted_top = dict(sorted(top.items(), key=lambda item: item[1], reverse=True))
        print(sorted_top)
        return list(sorted_top.keys())[:k]
