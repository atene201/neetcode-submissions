class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {')':'(', '}': '{', ']':'['}

        for c in s:
            print(c)
            if stack and c in brackets.keys() and brackets[c] == stack[-1]:
                stack.pop()
                continue
            stack.append(c)

        return len(stack) == 0
        