class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            if c in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                opening = stack.pop(len(stack) - 1)
                if opening == '[' and c != ']':
                    return False
                if opening == '{' and c != '}':
                    return False
                if opening == '(' and c != ')':
                    return False
        return len(stack) == 0