class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs: 
            char_count = [0] * 26 # a..z
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            key = tuple(char_count)
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
        r = []
        for v in res.values():
            r.append(v)
        return r