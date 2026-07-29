class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # build a hashtable with every word as a key and the index of its anagrams, if any, as values.
        anagram_map = {}
        r = []
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in anagram_map:
                anagram_map[s] = [strs[i]]
            else:
                anagram_map[s].append(strs[i])
        for v in anagram_map.values():
            r.append(v)
        return r
    
    def isAnagram(str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        freq = {}
        for c in str1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for c in str2:
            if c not in freq:
                return False
            freq[c] -= 1
        for v in freq.values():
            if v != 0:
                return False
        return True
