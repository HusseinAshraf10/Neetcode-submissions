class Solution:
    def isValid(self, s: str) -> bool:
        stack= []

        closeAndOpen= {")": "(", "}":"{", "]": "["}

        for c in s:
            # check if it's open parentheses
            if c not in closeAndOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeAndOpen[c]:
                    stack.pop()
                else:
                    return False

        return not stack
