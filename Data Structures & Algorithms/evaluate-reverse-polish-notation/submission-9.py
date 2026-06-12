class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        for token in tokens:
            if token == '+' and len(values) > 1:
                values.append(values.pop() + values.pop())
            elif token == '-' and len(values) > 1:
                small = values.pop()
                large = values.pop()
                values.append(large - small)
            elif token == '*' and len(values) > 1:
                values.append(values.pop() * values.pop())
            elif token == '/' and len(values) > 1:
                small = values.pop()
                large = values.pop()
                values.append(int(large / small))
            else:
                values.append(int(token))
        return values.pop()
        