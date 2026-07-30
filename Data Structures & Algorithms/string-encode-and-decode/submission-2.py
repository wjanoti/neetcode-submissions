class Solution:
    LIST_BEGIN = '\x01'
    LIST_END = '\x02'
    CHAR_DELIMITER = '\x03'

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += self.LIST_BEGIN
            for c in s:
                encoded_str += str(ord(c)) + self.CHAR_DELIMITER
            encoded_str += self.LIST_END
        return encoded_str

    def decode(self, s: str) -> List[str]:
        lists = []
        current_chars = []
        current_num = ""
        for c in s:
            if c == self.LIST_BEGIN:
                current_chars = []
                current_num = ""
            elif c == self.LIST_END:
                lists.append("".join(current_chars))
            elif c == self.CHAR_DELIMITER:
                current_chars.append(chr(int(current_num)))
                current_num = ""
            else:
                current_num += c
        return lists