class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1q: will the res array hold the number of days
        # before a warmer temp?

        # [ 10, 9, 8, 7, 11] 
        # res = [0, 0, 0, 1, 0]

        # loop through the temp arr
        # inner loop that uses that index were currently in to

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_top, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i))
        return res
