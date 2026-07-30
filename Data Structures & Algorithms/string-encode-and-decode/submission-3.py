class Solution:
    LIST_BEGIN = '\x01'
    LIST_END = '\x02'
    CHAR_DELIMITER = '\x03'

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i+length])
            i += length
        return result