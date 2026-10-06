class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            if i in pairs: 
                if not stack or stack[-1] != pairs[i]:
                    return False
                else:
                    stack.pop()
            else: 
                stack.append(i)

        return not stack
