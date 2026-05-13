class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
  
        for c in s:
            if c in brackets.values():
                # we've reached the part of the array that we'll need to start comparing
                if len(stack) != 0:   
                    if c == ')' and stack[-1] == '(':
                        stack.pop()
                        continue
                    if c == '}' and stack[-1] == '{':
                        stack.pop()
                        continue
                    if c == ']' and stack[-1] == '[':
                        stack.pop()
                        continue
                return False
            stack.append(c)
        print(stack)
        return len(stack) == 0    
        