class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        if len(s) != len(t):
            return False
        for c1 in s:
            char_map[c1] = char_map.get(c1, 0) + 1
        for c2 in t:
            if c2 in char_map:
                char_map[c2] -= 1
        for v in char_map.values():
            if v > 0:
                return False
        return True
            
        