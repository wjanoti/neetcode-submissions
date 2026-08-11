class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        for ch in t:
            if s_ptr == len(s):
                break
            if ch == s[s_ptr]:
                s_ptr += 1
        return s_ptr == len(s) 