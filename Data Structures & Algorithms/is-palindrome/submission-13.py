class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        print(l,r)
        while l < r:
            if not s[l].isalnum():
                print('here')
                l += 1
                continue
            if not s[r].isalnum():
                print('here2')
                r -= 1
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True