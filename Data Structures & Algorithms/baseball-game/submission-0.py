class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for num in operations:
            if num == '+' and len(stk) > 1:
                stk.append(stk[-1] + stk[-2])
            elif num == 'D' and len(stk) > 0:
                stk.append(2 * stk[-1])
            elif num == 'C' and len(stk) > 0:
                stk.pop()
            else:
                stk.append(int(num))
        return sum(stk)
            
            

        