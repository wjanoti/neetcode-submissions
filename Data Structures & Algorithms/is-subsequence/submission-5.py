class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if not s:
            return True
        s_ptr = 0
        for i in range(len(t)):
            if s_ptr == len(s) - 1:
                return True
            if t[i] == s[s_ptr]:
                s_ptr += 1
        return s_ptr == len(s) 