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

        # for c in s:
        #     if c in brackets.values():
        #         # we've reached the part of the array that we'll need to start comparing
        #         if len(stack) != 0:   
        #             if c == ')' and stack[-1] == '(':
        #                 stack.pop()
        #                 continue
        #             if c == '}' and stack[-1] == '{':
        #                 stack.pop()
        #                 continue
        #             if c == ']' and stack[-1] == '[':
        #                 stack.pop()
        #                 continue
        #         return False
        #     stack.append(c)
        # print(stack)
        # return len(stack) == 0    
        