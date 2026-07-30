class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_list = [[] for _ in range(len(nums) + 1)]
        top = {}
        for n in nums:
            top[n] = top.setdefault(n, 0) + 1
        
        for number, freq in top.items():
            top_list[freq].append(number)

        topK = []
        print(top_list)
        for i in range(len(top_list) - 1, 0, -1):
            if len(topK) >= k: 
                break
            if len(top_list[i]) == 0:
                continue

            for n in top_list[i]:
                topK.append(n)
                print(topK)
                print(len(topK))
                if len(topK) >= k:
                    break 
                
        return topK
